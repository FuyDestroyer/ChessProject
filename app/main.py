import pygame

pygame.init()

(width, height) = (480, 480)
screen = pygame.display.set_mode((width, height))

for i in range(8):
    for j in range(8):
        if((i+j) % 2 == 0):
            squareColor = (241, 212, 170)
        else:
            squareColor = (128, 76, 8)
        pygame.draw.rect(screen, squareColor, pygame.Rect(i*60, j*60, 60, 60))

img = pygame.image.load("C:\\Users\\SysC\\Pictures\\ChessPawn.png").convert()  
img.set_colorkey((255, 255, 255))
img = pygame.transform.scale(img,(60,60))
img2 = pygame.image.load("C:\\Users\\SysC\\Pictures\\ChessPawn2.png").convert()  
img2.set_colorkey((0,0,0))
img2 = pygame.transform.scale(img2, (60,60))

for p in range(8):
    screen.blit(img, (p*60, 60))
    screen.blit(img2, (p*60, 360))


pygame.display.flip()




#running section
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False