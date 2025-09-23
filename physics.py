from vectors import V

class Obj:
    """třída fyzických objektů - koulí"""
    def __init__(self, x, v, m, r = 0, Q = 0, col = "black"):
        if type(x) == V:
            self.pos = x
        else:
            self.pos = V(*x)
        if type(v) == V:
            self.vel = v
        else:
            self.vel = V(*v)
        self.acc = V.zero()
        self.mass = m
        self.radius = r
        self.charge = Q
        self.color = col

class Universe:
    def __init__(self, g_const, el_const):
        self.objects = []
        self.time = 0
        self.g_const = g_const
        self.el_const = el_const
    
    def __getitem__(self, i):
        return(self.objects[i])

    def cycle(self, t):
        """provedu jednu iteraci simulace"""
        self.acc_reset()
        self.dynamics()
        self.kinematics(t)

    def kinematics(self, t):
        """pohne koulemi za daný čas podle jejich rychlostí a zrychlení"""
        for o in self:
            o.pos += (t * o.vel) + (((t**2) / 2) * o.acc)
            o.vel += t * o.acc
        self.time += t

    def acc_reset(self):
        for o in self:
            o.acc = V.zero()

    def dynamics(self):
        """spočte zrychlení, kterým na sebe koule působí"""
        i = 1
        for o1 in self:
            for o2 in self[i:]:
                relpos = o2.pos - o1.pos
                distance = abs(relpos)
                magic_v = relpos / (distance**3)   #vystupuje v gravitační  i elektrické síle
                self.gravity(o1, o2, magic_v)
                self.electr(o1, o2, magic_v)
            i += 1

    def gravity(self, o1, o2, magic_v):
        """gravitační působení dvou koulí"""
        g_vect = self.g_const * magic_v
        o1.acc += o2.mass * g_vect
        o2.acc -= o1.mass * g_vect

    def electr(self, o1, o2, magic_v):
        """elektrostatické působení s další koulí"""
        force = self.el_const * o1.charge * o2.charge * magic_v
        o1.acc -= force / o1.mass
        o2.acc += force / o2.mass

    def create(self, x, v, m = 1, r = 0, Q = 0, col = "black"):
        """vytvoří kouli"""
        self.objects.append(Obj(x, v, m, r, Q, col))

    def centrum(self, balls = None):
        """najde těžiště"""
        if balls == None:
            balls = self.objects
        centr = V.zero()
        mass = 0
        for o in balls:
            mass_i = o.mass
            centr += mass_i * o.pos
            mass += mass_i
        return(centr / mass)
