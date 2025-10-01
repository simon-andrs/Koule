"""
Hodnoty z: Simó, C.(2001). New families of solutions in N-body problems. In European Congress of Mathematics: Barcelona, July 10--14, 2000, Volume I (pp.101-115). Birkhäuser Basel.
Počítáno v jednorozměrném komplexním prostoru - při reálném čase odpovídá dvourozměrnému reálnému.
Časový krok má však malou komplexní složku, která způsobuje pomalé odchylování od dvourozměrného modelu.
"""

from main import Main

m = Main(dim = 1, deltat = 0.001 + 0.000001j, g_const = 1)
m.obj((0.995492,), (-0.695804/2 - 1.067860/2 * 1j,), r = 0.02, col = 'blue')
m.obj((-0.995492,), (-0.695804/2 - 1.067860/2 * 1j,), r = 0.02, col = 'red')
m.obj((0,), (0.695804 + 1.067860j,), r = 0.02, col = 'green')

m.run()

