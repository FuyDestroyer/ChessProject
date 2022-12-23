import pygame

pygame.init()

(width, height) = (480, 480)
screen = pygame.display.set_mode((width, height))


   


#Object class

       



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


class ChessPiece:
    def Update_Position(self,x):
         screen.blit(img,y)






pygame.display.flip()




#running section
running = True
while running:

    
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    elif event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        if 0<pos[1]<59:
            if 0<pos[0]<59:
                square = 18
            elif 60<pos[0]<119:
                square = 28
            elif 120<pos[0]<179:
                square = 38
            elif 180<pos[0]<239:
                square = 48
            elif 240<pos[0]<299:
                square = 58
            elif 300<pos[0]<359:
                square = 68
            elif 360<pos[0]<419:
                square = 78
            elif 420<pos[0]<480:
                square = 88
        elif 60<pos[1]<119:
            if 0<pos[0]<59:
                square = 17
            elif 60<pos[0]<119:
                square = 27
            elif 120<pos[0]<179:
                square = 37
            elif 180<pos[0]<239:
                square = 47
            elif 240<pos[0]<299:
                square = 57
            elif 300<pos[0]<359:
                square = 67
            elif 360<pos[0]<419:
                square = 77
            elif 420<pos[0]<480:
                square = 87
        elif 120<pos[1]<179:
            if 0<pos[0]<59:
                square = 16
            elif 60<pos[0]<119:
                square = 26
            elif 120<pos[0]<179:
                square = 36
            elif 180<pos[0]<239:
                square = 46
            elif 240<pos[0]<299:
                square = 56
            elif 300<pos[0]<359:
                square = 66
            elif 360<pos[0]<419:
                square = 76
            elif 420<pos[0]<480:
                square = 86
        elif 180<pos[1]<239:
            if 0<pos[0]<59:
                square = 15
            elif 60<pos[0]<119:
                square = 25
            elif 120<pos[0]<179:
                square = 35
            elif 180<pos[0]<239:
                square = 45
            elif 240<pos[0]<299:
                square = 55
            elif 300<pos[0]<359:
                square = 65
            elif 360<pos[0]<419:
                square = 75
            elif 420<pos[0]<480:
                square = 85
        elif 240<pos[1]<299:
            if 0<pos[0]<59:
                square = 14
            elif 60<pos[0]<119:
                square = 24
            elif 120<pos[0]<179:
                square = 34
            elif 180<pos[0]<239:
                square = 44
            elif 240<pos[0]<299:
                square = 54
            elif 300<pos[0]<359:
                square = 64
            elif 360<pos[0]<419:
                square = 74
            elif 420<pos[0]<480:
                square = 84
        elif 300<pos[1]<359:
            if 0<pos[0]<59:
                square = 13
            elif 60<pos[0]<119:
                square = 23
            elif 120<pos[0]<179:
                square = 33
            elif 180<pos[0]<239:
                square = 43
            elif 240<pos[0]<299:
                square = 53
            elif 300<pos[0]<359:
                square = 63
            elif 360<pos[0]<419:
                square = 73
            elif 420<pos[0]<480:
                square = 83
        elif 360<pos[1]<419:
            if 0<pos[0]<59:
                square = 12
            elif 60<pos[0]<119:
                square = 22
            elif 120<pos[0]<179:
                square = 32
            elif 180<pos[0]<239:
                square = 42
            elif 240<pos[0]<299:
                square = 52
            elif 300<pos[0]<359:
                square = 62
            elif 360<pos[0]<419:
                square = 72
            elif 420<pos[0]<480:
                square = 82
        elif 420<pos[1]<480:
            if 0<pos[0]<59:
                square = 11
            elif 60<pos[0]<119:
                square = 21
            elif 120<pos[0]<179:
                square = 31
            elif 180<pos[0]<239:
                square = 41
            elif 240<pos[0]<299:
                square = 51
            elif 300<pos[0]<359:
                square = 61
            elif 360<pos[0]<419:
                square = 71
            elif 420<pos[0]<480:
                square = 81 

        
            

        
