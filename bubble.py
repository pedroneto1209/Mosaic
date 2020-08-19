import pygame
from random import randint, choice
import math

pygame.init()
width = 1280
height = 600
lugares = []
screen = pygame.display.set_mode((width, height))
circles = []
img = pygame.image.load(r'C:\Users\pedro\OneDrive\Imagens\LETUVS.png')
for x in range(width):
    for y in range(height):
        imgcor = img.get_at((x, y))
        if imgcor == (255, 255, 255, 255):
            lugares.append([x, y])

def map(n, start1, stop1, start2, stop2):
    return ((n-start1)/(stop1-start1))*(stop2-start2)+start2

class Circle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.raio = 1
        self.crescendo = True
        self.cor = (255, map(self.x, 0, width, 50, 102), map(self.x, 0, width, 100, 200))

    def draw(self):
        pygame.draw.circle(screen, self.cor, (self.x, self.y), int(self.raio), 1)

    def cresce(self):
        if self.crescendo:
            self.raio += 1

    def outro(self):
        for c in circles:
                dist = math.sqrt((self.x-c.x)**2 + (self.y-c.y)**2)
                if (dist >= c.raio + self.raio):
                    return True
                else:
                    return False

    def bateu(self):
        return (self.y + self.raio > height or self.y < self.raio or self.x + self.raio > width or self.x < self.raio)


def novocirc():
    sup = choice(lugares)
    x = sup[0]
    y = sup[1]

    valido = True

    for c in circles:
        if(math.sqrt((x-c.x)**2 + (y-c.y)**2) < c.raio):
            valido = False
            break
    
    if valido:
        return Circle(x, y)
    else:
        return None

loop = True
jupi = True
while loop:

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()

    contagem = 0
    total = 10
    tentativas = 0
    
    while contagem < total and jupi:
        circle = novocirc()
        if circle != None:
            circles.append(circle)
            contagem += 1
        else:
            tentativas += 1

    if tentativas > 40:
        jupi = False

    mous, _ = pygame.mouse.get_pos()
    
    for c in circles:
        #c.cor = (255, map(mous, 0, width, 0, 255), c.cor[2])
        if c.crescendo:
            if c.bateu():
                c.crescendo = False
            else:
                for out in circles:
                    if c != out:
                        dist = math.sqrt((out.x-c.x)**2 + (out.y-c.y)**2)
                        if dist < c.raio + out.raio:
                            c.crescendo = False
                            break


        c.draw()
        c.cresce()

    pygame.display.update()
    screen.fill((0, 0, 0))


