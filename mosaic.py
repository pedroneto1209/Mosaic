import pygame
from Media import dicio

pygame.init()
width = 411
height = 411
sqr = 10
screen = pygame.display.set_mode((width, height))
img = pygame.image.load(r'C:\Users\pedro\OneDrive\Imagens\mosaic2.png')

larg = int(width/sqr)
alt = int(height/sqr)

for i in range(larg):
    for j in range(alt):
        r, g, b = 0, 0, 0   
        for x in range(sqr):
            for y in range(sqr):
                r += img.get_at((x + i*sqr, y + j*sqr))[0]
                g += img.get_at((x + i*sqr, y + j*sqr))[1]
                b += img.get_at((x + i*sqr, y + j*sqr))[2]

        r /= sqr**2
        g /= sqr**2
        b /= sqr**2

        melhor = 9999999999999
        imp = []

        for a in dicio['media']:
            calc = abs(r - a[0] + g - a[1] + b - a[2])
            if calc < melhor:
                melhor = calc
                imp = dicio['imagem'][dicio['media'].index(a)]
            
        surface = pygame.Surface((32, 32))
        for p in range(32):
            for l in range(32):
                rr = imp[p + 32*l]
                gg = imp[p + 32*l + 1024]
                bb = imp[p + 32*l + 2048]
                
                surface.set_at((p, l), (rr, gg, bb))
                surface = pygame.transform.scale(surface, (sqr, sqr))

        screen.blit(surface, (i*sqr, j*sqr))

pygame.display.flip()
                
while 1:

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()
