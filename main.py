class Main:
    def __init__(self, dim = 2, deltat = 1, g_const = 6.6743 * 10**(-11), el_const = 8.9875 * 10**9, screen = (1400, 800), back_color = "white"):
        from vectors import V
        V.dim = dim
        from physics import Obj, Universe
        from graphics import Graph
        self.space = Universe(g_const, el_const)
        self.graphics = Graph(self.space, dim, deltat, screen, back_color)
        self.zero = V.zero()

    def obj(self, x, v, m = 1, r = 0, Q = 0, col = "black"):
        """vytvoří objekt"""
        self.space.create(x, v, m, r, Q, col)

    def run(self):
        """spustí simulaci"""
        self.graphics.focus()
        while True:
            if not self.graphics.paused:
                self.space.cycle(self.graphics.deltat)
            self.graphics.cycle()
