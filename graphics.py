from vectors import V
import pygame

class Graph:
    
    def __init__(self, space, dim, deltat, screen, back_color = "white"):
        self.space = space   #soubor objektů, který zobrazuji
        self.dim = dim   #počet dimenzí
        self.screen = screen   #velikost okna ve kterém zobrazuji
        self.deltat = deltat   #délka kroku simulace
        self.camera = V.zero()   #pozice kamery (vektor)
        self.back_color = back_color   #barva pozadí
        self.paused = False   #je pozastavený čas?
        self.D3 = (dim >= 3)
        self.zoom = 1
        pygame.init()
        self.window = pygame.display.set_mode(screen)
        self.window.fill(back_color)

    def cycle(self):
        """zkontroluje ovládání a zobrazí objekty"""
        self.control()
        self.display()
        self.draw()

    def display(self):
        """zobrazení všech koulí"""
        #self.drawball(self.space.centrum(), 3, "blue", abssize=True)
        for o in self.space:
            self.drawball(o, o.radius, o.color)

    def relative_pos(self, ball):
        """vrátí zobrazovanou pozici dané koule"""
        vector = self.zoom * (ball.pos - self.camera)
        x = vector[0].real
        if self.dim == 1:
            y = vector[0].imag
        else:
            y = vector[1].real
        if self.D3:
            z = vector[2].real
            return(x,y,z)
        else:
            return(x,y)

    def relative_size(self, ball):
        """vrátí zobrazovanou velikost dané koule"""
        return(ball.radius * self.zoom)
    
    def drawball(self, ball, r, color="black", abssize=False):
        """spočítá, jak se má daná koule zobrazit"""
        scr, camera = self.screen, self.camera
        relative = self.relative_pos(ball)   #zobrazovaná pozice koule (vektor)
        x, y = relative[0], relative[1]
        if not(abssize):
            r = self.relative_size(ball)   #zdánlivá velikost koule
            if r < 1:   #pokud by se zobrazovala příliš malá
                r = 1
                color = "black"
        if abs(x) <= r + scr[0] / 2:   #je objekt v zobrazovaném poli?
            if not self.D3:
                if abs(y) <= r + scr[1] / 2:
                    self.circle((x, y), r, color)
            else:
                lnp = self.linepos
                z = relative[2]
                if abs(z) <= r + lnp / 2:
                    self.circle((x, z), r, color, view = 1)
                if abs(y) <= r + (scr[1] - lnp) / 2:
                    self.circle((x, y), r, color, view = 2)
    
    def circle(self, mid, r, color = "black", view = 0):
        """nakreslí kruh"""
        wnd, scr = self.window, self.screen
        if view > 0:
            lnp = self.linepos
        if view == 0:   #2D zobrazení
            pygame.draw.circle(wnd, color, (scr[0] / 2 + mid[0], scr[1] / 2 - mid[1]), r)
        elif view==1:   #nárys
            pygame.draw.circle(wnd, color, (scr[0] / 2 + mid[0], lnp / 2 - mid[1]), r)
        else:   #půdorys
            pygame.draw.circle(wnd, color, (scr[0] / 2 + mid[0], lnp + (scr[1] - lnp)/2 - mid[1]), r)
    
    def control(self):
        """
        ovládání klávesnicí:
        W/S: zoom
        šipky a crtl/tečka: pohyb kamery
        E/Q: rychlost (délka kroku)
        P/G: zastaví/obnoví pohyb
        X/C: pustí čas dozadu/dopředu
        H/B: pohybuje dělící čarou (jen ve 3 dimenzích)
        A: změní kameru a přiblížení, aby byly vidět všechny objekty
        esc: ukončí program
        """
        zoom_delta = 0.001
        move_delta = 0.1
        deltat_delta = 0.001
        line_delta = 0.3
        keys = pygame.key.get_pressed()
        deltat, zoom, screen, dim = self.deltat, self.zoom, self.screen, self.dim
        if self.D3:
            linepos = self.linepos
        
        if keys[pygame.K_w]:
            self.zoom *= 1 + zoom_delta
        if keys[pygame.K_s]:
            self.zoom *= 1 - zoom_delta
        if keys[pygame.K_RIGHT]:
            self.camera += (move_delta / zoom) * V.direct(0)
        if keys[pygame.K_LEFT]:
            self.camera -= (move_delta / zoom) * V.direct(0)
        if keys[pygame.K_UP]:
            if dim == 1:
                self.camera += (move_delta / zoom) * V.direct(0) * 1j
            else:
                self.camera += (move_delta / zoom) * V.direct(1)
        if keys[pygame.K_DOWN]:
            if dim == 1:
                self.camera -= (move_delta / zoom) * V.direct(0) * 1j
            else:
                self.camera -= (move_delta / zoom) * V.direct(1)
        if keys[pygame.K_PERIOD]:
            if self.D3:
                self.camera += (move_delta / zoom) * V.direct(2)
        if keys[pygame.K_RCTRL]:
            if self.D3:
                self.camera -= (move_delta / zoom) * V.direct(2)
        if keys[pygame.K_e]:
            self.deltat *= 1 + deltat_delta
        if keys[pygame.K_q]:
            self.deltat *= 1 - deltat_delta
        if keys[pygame.K_p]:
            self.paused = True
        if keys[pygame.K_g]:
            self.paused = False
        if keys[pygame.K_x]:
            if deltat.real > 0 or (deltat.real == 0 and deltat.imag > 0):
                self.deltat *= -1
        if keys[pygame.K_c]:
            if deltat.real < 0 or (deltat.real == 0 and deltat.imag < 0):
                self.deltat *= -1
        if keys[pygame.K_b]:
            if self.D3:
                if linepos < screen[1]:
                    self.linepos += line_delta
        if keys[pygame.K_h]:
            if self.D3:
                if linepos > 0:
                    self.linepos -= line_delta
        if keys[pygame.K_a]:
            self.focus()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
    
    def draw(self):
        """samotné vykreslení pomocí pygame"""
        wnd, scr, bcol = self.window, self.screen, self.back_color
        if self.D3:
            lnp = self.linepos
            pygame.draw.line(wnd, "black", (0, lnp), (scr[0], lnp))
        pygame.display.update()
        wnd.fill(bcol)
        pygame.event.get()

    def focus(self):
        """automaticky změní pozici a přiblížení kamery"""
        fill = 0.5   #jak velká čast obrazovky se zaplní
        if len(self.space.objects) == 0:
            self.zoom = 1
            self.camera = V.zero()
            return
        inf = (float('inf'), float('-inf'))
        xlim, ylim, zlim = inf, inf, inf
        for o in self.space:
            v = self.relative_pos(o)
            r = self.relative_size(o)
            xlim = (min(xlim[0], v[0] - r), max(xlim[1], v[0] + r))
            ylim = (min(ylim[0], v[1] - r), max(ylim[1], v[1] + r))
            if self.D3:
                zlim = (min(zlim[0], v[2] - r), max(zlim[1], v[2] + r))
        camera = [sum(xlim) / 2, sum(ylim) / 2]
        if self.D3:
            camera.append(sum(zlim) / 2)
            camera += [0] * (self.dim - 3)
        elif self.dim == 1:
            camera = (camera[0] + camera[1] * 1j,)
        self.camera += V(*camera) / self.zoom
        xdif = xlim[1] - xlim[0]
        ydif = ylim[1] - ylim[0]
        if not self.D3:
            mindif = min(self.screen[0] / xdif, self.screen[1] / ydif)
        else:
            zdif = zlim[1] - zlim[0]
            self.linepos = self.screen[1] * zdif / (ydif + zdif)
            mindif = min(self.screen[0] / xdif, self.linepos / zdif)
        self.zoom *= fill * mindif
