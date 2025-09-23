class V:
    """třída pro práci s vektory"""
    dim = 7
    
    def __init__(self, *value):
        if len(value) != self.dim:
            raise ValueError("wrong vector dimension")
        self.p = tuple(value)
    
    def __str__(self):
        return("v:" + str(self.p))
    
    def __getitem__(self, i):
        return(self.p[i])
    
    def __add__(self, other):
        """součet vektorů"""
        if type(other) != V:
            raise TypeError("can only add vector to other vector")
        sum = []
        i = 0
        for part in self:
            sum.append(part + other[i])
            i += 1
        return(V(*sum))
    
    def __rmul__(self, number):
        """násobení vektoru číslem"""
        prod = []
        for part in self:
            prod.append(number * part)
        return(V(*prod))
    
    def __matmul__(self, other):
        """skalární součin - pomocí @"""
        prod = 0
        i = 0
        for part in self:
            prod += part.conjugate() * other[i]
            i += 1
        return(prod)
    
    def __mul__(self, number):
        return(number * self)
    
    def __neg__(self):
        return(-1 * self)
    
    def __sub__(self, other):
        return(self + (-other))
    
    def __truediv__(self, number):
        """dělení vektoru číslem"""
        return((1 / number) * self)
    
    def __abs__(self):
        """velikost vektoru"""
        return((self @ self).real ** 0.5)

    @classmethod
    def zero(cls):
        """nulový vektor"""
        return cls(*(cls.dim * [0]))
    
    @classmethod
    def direct(cls, part):
        """jednotkový vektor v dané ose"""
        return(cls(*(part * [0] + [1] + (cls.dim - part - 1)*[0])))
