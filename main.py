from math import*
import pygame
import random

def projection(p):
    x, y, z = p
    return (x+350), ((z-y)/sqrt(2)+400)
#-z/2

class Triangle:
    
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        
    
    def rotate_tri(self , axe):
        global rotate
        if rotate:
            self.p1 = rotation(self.p1, 0.1, axe[0], axe[1])
            self.p2 = rotation(self.p2, 0.1, axe[0], axe[1])
            self.p3 = rotation(self.p3, 0.1, axe[0], axe[1])
    
    
    def draw(self, screen, color):
        z1 = self.p1[2]
        z2 = self.p2[2]
        z3 = self.p3[2]
        mz = (z1+z2+z3)/3
        p1 = projection(self.p1)
        p2 = projection(self.p2)
        p3 = projection(self.p3)
        return [p1, p2, p3, mz]
#
        
#         pygame.draw.line(screen, color, p1, p2, 2)
#         pygame.draw.line(screen, color, p2, p3, 2)
#         pygame.draw.line(screen, color, p3, p1, 2)
        
        
class Carre:
    def __init__(self, points, size, center):
        self.t1 = Triangle(points[0], points[1], points[2])
        self.t2 = Triangle(points[3], points[4], points[5])
        self.size = size
        self.center = center
        self.c = [self.t1, self.t2]
        
    
    def get_translated(self, v):
        t1 = Triangle(self.t1.p1, self.t1.p2, self.t1.p3)
        t2 = Triangle(self.t2.p1, self.t2.p2, self.t2.p3)
        t1.p1 = (t1.p1[0] + v[0], t1.p1[1] + v[1], t1.p1[2] + v[2]) 
        t1.p2 = (t1.p2[0] + v[0], t1.p2[1] + v[1], t1.p2[2] + v[2]) 
        t1.p3 = (t1.p3[0] + v[0], t1.p3[1] + v[1], t1.p3[2] + v[2]) 
        t2.p1 = (t2.p1[0] + v[0], t2.p1[1] + v[1], t2.p1[2] + v[2]) 
        t2.p2 = (t2.p2[0] + v[0], t2.p2[1] + v[1], t2.p2[2] + v[2]) 
        t2.p3 = (t2.p3[0] + v[0], t2.p3[1] + v[1], t2.p3[2] + v[2])
        points = [t1.p1, t1.p2, t1.p3, t2.p1, t2.p2, t2.p3]
        return Carre(points, size, center)
    
    def get_rotated_v(self, r):
        t1 = Triangle(self.t1.p1, self.t1.p2, self.t1.p3)
        t2 = Triangle(self.t2.p1, self.t2.p2, self.t2.p3)
        t1.p1 = (t1.p1[0], t1.p1[1], t1.p1[2]) 
        t1.p2 = (t1.p1[0], t1.p2[1], t1.p2[2] + r) 
        t1.p3 = (t1.p1[0], t1.p3[1], t1.p3[2]) 
        t2.p1 = (t1.p1[0], t2.p1[1], t2.p1[2] + r) 
        t2.p2 = (t1.p1[0], t2.p2[1], t2.p2[2] + r) 
        t2.p3 = (t1.p1[0], t2.p3[1], t2.p3[2])
        points = [t1.p1, t1.p2, t1.p3, t2.p1, t2.p2, t2.p3]
        return Carre(points, size, center)
    
    def get_rotated_h(self, r):
        t1 = Triangle(self.t1.p1, self.t1.p2, self.t1.p3)
        t2 = Triangle(self.t2.p1, self.t2.p2, self.t2.p3)
        t1.p1 = (t1.p1[0], t2.p2[1], t1.p1[2]) 
        t1.p2 = (t1.p2[0], t2.p2[1], t1.p2[2]) 
        t1.p3 = (t1.p3[0], t2.p2[1], t1.p3[2] + r) 
        t2.p1 = (t2.p1[0], t2.p2[1], t2.p1[2] + r) 
        t2.p2 = (t2.p2[0], t2.p2[1], t2.p2[2]) 
        t2.p3 = (t2.p3[0], t2.p2[1], t2.p3[2] + r)
        points = [t1.p1, t1.p2, t1.p3, t2.p1, t2.p2, t2.p3]
        return Carre(points, size, center)
        
    def rotate(self, axe):
        self.t1.rotate_tri(axe)
        self.t2.rotate_tri(axe)

        
    def draw_carre(self):

        t1 = self.t2.draw(screen, RED)
        t2 = self.t1.draw(screen, BLUEb)
        return [t1, t2]

        
class Cube:
    

    def __init__(self, carre, axe):
        self.carre = carre
        self.carre2 = carre.get_translated([0, 0, carre.size])
        self.carre3 = carre.get_rotated_v(carre.size)
        self.carre4 = self.carre3.get_translated([carre.size, 0, 0])
        self.carre5 = carre.get_rotated_h(carre.size)
#         self.carre6 = self.carre2.get_rotated_h(carre.size) #sol du cube
        self.axe = axe
        
    def draw(self):
        self.carre.rotate(self.axe)
        self.carre2.rotate(self.axe)
        self.carre3.rotate(self.axe)
        self.carre4.rotate(self.axe)
        self.carre5.rotate(self.axe)
#         self.carre6.rotate(self.axe)
        res = []
        res += self.carre.draw_carre()
        res += self.carre2.draw_carre()
        res += self.carre3.draw_carre()
        res += self.carre4.draw_carre()
        res += self.carre5.draw_carre()
#         res += self.carre6.draw_carre()
        return res
        

class Pyramide:
    
    def __init__(self, base, h, cx, cy):
        self.cx = cx
        self.cy = cy
        self.base = base
        self.ph = [cx, base.t1.p1[1] + h, cy]
        
    def draw(self):
        global BLUEb, RED
        self.base.rotate((self.cx, self.cy))
        pygame.draw.polygon(screen, BLUEb, (projection(self.base.t1.p1), projection(self.ph), projection(self.base.t1.p3)), 0)
        pygame.draw.polygon(screen, RED, (projection(self.base.t1.p2), projection(self.ph), projection(self.base.t1.p1)), 0)
        pygame.draw.polygon(screen, YELLOW, (projection(self.base.t1.p3), projection(self.ph), projection(self.base.t2.p1)), 0)
        pygame.draw.polygon(screen, LGREY, (projection(self.base.t2.p1), projection(self.ph), projection(self.base.t2.p2)), 0)
#         pygame.draw.line(screen, BLUEb, projection(self.base.t1.p1), projection(self.ph), 2)
#         pygame.draw.line(screen, RED, projection(self.base.t1.p2), projection(self.ph), 2)
#         pygame.draw.line(screen, BLUEb, projection(self.base.t1.p3), projection(self.ph), 2)
#         pygame.draw.line(screen, RED, projection(self.base.t2.p1), projection(self.ph), 2)
        self.base.draw_carre()

class Painter:
    
    def __init__(self):
        self.t = 0
        
    def draw(self, triangles):
        triangles.sort(key = lambda x: x[3])
        
        colors = [RED, BLUEb, PINK, GREY]*12
        idx = 0
        g = 0
        for triangle in triangles:
            p1, p2, p3, z = triangle
#             pygame.draw.polygon(screen, (colors[idx][0]+g, colors[idx][1]+g, colors[idx][2]+g), (p1, p2, p3), 0)
            pygame.draw.polygon(screen, RED, (p1, p2, p3), 0)
            pygame.draw.polygon(screen, BLUEb, (p1, p2, p3), 4)
#             (colors[idx+1][0], colors[idx+1][1], colors[idx+1][2])
            idx = (idx+1)
            if idx%4 == 0:
                g = 0
            else:
                g -= 10
        
painter = Painter()

#lance pygame
pygame.init()

#definis les fps
clock = pygame.time.Clock()
FPS = 60

screen_w = 1300
screen_h = 690
screen = pygame.display.set_mode((screen_w, screen_h))

#couleurs
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (50, 50, 50)
LGREY = (128, 128, 128)
BLUE = (0, 0, 255)
BLUEb = (31, 176, 245)
PINK = (255, 132, 143)

#images
pause = pygame.image.load("pause.png")
skipd = pygame.image.load("skipd.png")
skipg = pygame.image.load("skipg.png")
fond = pygame.image.load("fond.png")
pyr = pygame.image.load("pyr.png")
cub = pygame.image.load("cub.png")
sfond = pygame.transform.scale(fond, (screen_h, screen_h))

#fonts
fps_font = pygame.font.Font(None, 20)
    
#conditions
rotate = True
dpyr = False
dcub = True

def rotation(p, a, cx, cy):
    px = p[0] - cx #400
    py = p[1]
    pz = p[2] - cy #100
    px1 = px * cos(a) + pz * sin(a) + cx
    py1 = py
    pz1 = px * -sin(a) + pz * cos(a) + cy
    return px1, py1, pz1

def draw_text(text, font, color, x, y):
    text = font.render(text, True, color)
    screen.blit(text, (x, y))

centerb = (200, 300)
center = (350, 200)
centerd = (375, 150)
centerc = (200, 100)
centree = (600, 300)
sizee = 200
size = 100
sizeb = 200
sized = 50


def coord_cube(center, size):
    t1p1 = [center[0], center[1], 0]
    t1p2 = [size + center[0], center[1], 0]
    t1p3 = [center[0], center[1]-size, 0]
    t2p1 = [size + center[0], center[1]-size, 0]
    t2p2 = [size + center[0], center[1], 0]
    t2p3 = [center[0], center[1]-size, 0]
    points = [t1p1, t1p2, t1p3, t2p1, t2p2, t2p3]
    return points

def coord_base(center, size):
    t1p1 = [center[0], center[1], 0]
    t1p2 = [size + center[0], center[1], 0]
    t1p3 = [center[0], center[1], size]
    t2p1 = [size + center[0], center[1], size]
    t2p2 = [size + center[0], center[1], 0]
    t2p3 = [center[0], center[1], size]
    points = [t1p1, t1p2, t1p3, t2p1, t2p2, t2p3]
    return points


points = coord_cube(center, size)
points2 = coord_cube(centerb, sizeb)
points3 = coord_cube(centerd, sized)
points4 = coord_base(centerc, sizeb)
points5 = coord_base(centree, sizee)

c = Carre(points, size, center)
c2 = Carre(points2, sizeb, centerb)
c3 = Carre(points3, sized, centerd)
cube = Cube(c, (400,50))
cube2 = Cube(c2, (300,100))
cube3 = Cube(c3, (400,25))

b = Carre(points4 , sizeb, (200 , 100))
b2 = Carre(points5 , sizee, (600 , 300))
p = Pyramide(b, 300, 300, 100)
p2  = Pyramide(b2, -300, 700, 100)

runing = True
while runing:
    
    #limite les fps
    clock.tick(FPS)
     
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, GREY, (screen_w - 350, 0, screen_w*(1/3)-50, screen_h), border_radius=0)
    pygame.draw.rect(screen, LGREY, (screen_w - 325, 15, screen_w*(1/3)-100, screen_h-30), border_radius=20)

    draw_text(str(FPS), fps_font, WHITE, 5, 5)
    
    spause = pygame.transform.scale(pause, (50, 50))
    screen.blit(spause, (screen_w/6-25, 25))
    sskipd = pygame.transform.scale(skipd, (50, 50))
    screen.blit(sskipd, (screen_w/6+75, 25))
    sskipg = pygame.transform.scale(skipg, (50, 50))
    screen.blit(sskipg, (screen_w/6-125, 25))
    screen.blit(sfond, (250, 0))
    spyr = pygame.transform.scale(pyr, (100, 100))
    screen.blit(spyr, (1000, 100))
    scub = pygame.transform.scale(cub, (100, 100))
    screen.blit(scub, (1000, 250))
    key=pygame.key.get_pressed()
    
    if dcub:
    #c.draw_cube()
#     cube.draw()
        painter.draw(cube2.draw())
#     cube3.draw()
    if dpyr:
        p.draw()
#     p2.draw()
    
    #mise à jour de l'affichage
    pygame.display.update()
    
    #gestion d'evènement
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
        elif (event.type == pygame.MOUSEBUTTONUP and event.button == 1):
            menu_mouse_pos = pygame.mouse.get_pos()
            if (screen_w/6-25 <= menu_mouse_pos[0] <= screen_w/6+25 and 25 <= menu_mouse_pos[1] <= 75):
                if rotate: #a corriger
                    rotate = False
                else:
                    rotate = True
            if (screen_w/6-125 <= menu_mouse_pos[0] <= screen_w/6-75 and 25 <= menu_mouse_pos[1] <= 75):
                FPS = FPS - 5
            if (screen_w/6+75 <= menu_mouse_pos[0] <= screen_w/6+125 and 25 <= menu_mouse_pos[1] <= 75) :
                FPS = FPS + 5
            if (screen_w*.7+90 <= menu_mouse_pos[0] <= screen_w*.7+190 and 100 <= menu_mouse_pos[1] <= 200):
                dpyr = not dpyr
            if (screen_w*.7+90 <= menu_mouse_pos[0] <= screen_w*.7+190 and 250 <= menu_mouse_pos[1] <= 350):
                dcub = not dcub
                
        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if rotate:
                        rotate = False
                    else:
                        rotate = True
                elif event.key == pygame.K_LEFT:
                    FPS = FPS - 5
                elif event.key == pygame.K_RIGHT:
                    FPS = FPS + 5

#sort de pygame
pygame.quit()