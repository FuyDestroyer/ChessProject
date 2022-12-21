import pygame

pygame.init()


(width, height) = (480, 480)
screen = pygame.display.set_mode((width, height))
for x in range(4):
    Top = 120*x
    for i in range(4):
        Lefta = 120*i
        Leftb = Lefta + 60
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(Lefta, Top, 60, 60))
        pygame.draw.rect(screen, (128, 76, 8), pygame.Rect(Leftb, Top, 60, 60))
for x in range(4):
    Top = 120*x+60
    for i in range(4):
        Lefta = 120*i
        Leftb = Lefta + 60
        pygame.draw.rect(screen, (128, 76, 8), pygame.Rect(Lefta, Top, 60, 60))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(Leftb, Top, 60, 60))
img = pygame.image.load("C:\\Users\\SysC\\Pictures\\ChessPawn.png").convert()  
img.set_colorkey((255, 255, 255))
Pawn=(60,60)
img = pygame.transform.scale(img, Pawn)
screen.blit(img, (0, 60))     
pygame.display.flip()





#running section
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False