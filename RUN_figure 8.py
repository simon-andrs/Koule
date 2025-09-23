from main import Main

m = Main(dim = 2, deltat = 0.001, g_const = 1)
m.obj((0.995492, 0), (-0.695804/2,-1.067860/2), r = 0.02, col = 'blue')
m.obj((-0.995492, 0), (-0.695804/2,-1.067860/2), r = 0.02, col = 'red')
m.obj((0, 0), (0.695804,1.067860), r = 0.02, col = 'green')

m.run()
