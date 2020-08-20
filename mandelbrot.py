import pygame

pygame.init()
width = 700
height = 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Mandelbrot Set')
maxit = 100

def mapp(n, start1, stop1, start2, stop2):
    return ((n-start1)/(stop1-start1))*(stop2-start2)+start2

def main():
    for i in range(width):
        for j in range(height):
            d = 2
            a = mapp(i, 0, width, -d, d)
            b = mapp(j, 0, height, -d, d)

            ca = a
            cb = b
            n = 0

            while n < maxit:
                aa = a*a - b*b
                bb = 2*a*b
                a = aa + ca
                b = bb + cb
                if abs(a + b) > 16:
                    break
                n += 1

            b = mapp(n, 0, maxit, 0, 255)
            
            bright = (0, 0, b)

            if n == maxit:
                bright = (0 , 0, 0)
            
            screen.set_at((i, j), bright)

pygame.image.save(screen, "aaa.png")

main()

while 1:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
