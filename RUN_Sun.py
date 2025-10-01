"""3D simulace Slunce a 3 družic se stejnou oběžnou dobou jako Země"""

from main import Main
m = Main(dim = 3, deltat = 2000)


m.obj((0, 0, 0), (0, 0, 0), m = 1.988 * 10**30, r = 6.957 * 10**8,col = 'red')
m.obj((-1.621 * 10**11, 0, 2.808 * 10**10),(0, 26941, 0))
m.obj((-1.327 * 10**11, 0, -2.298 * 10**10),(0, 32928, 0))
m.obj((-1.496 * 10**11, 0, 0), (0, 29784, 0))

m.run()

