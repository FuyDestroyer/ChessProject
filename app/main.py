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
    def __init__(self, color, currentsquare):
        self.color = color
        self.square = currentsquare
class Pawn:
    def __init__(self, color, currentsquare, moved):
        super().__init__(color, currentsquare)
        self.moved = moved
class King:
    def __init__(self, color, currentsquare, moved, checked):
        super().__init__(color, currentsquare)
        self.moved = moved
        self.checked = checked
class Night:
    def __init__(self, color, currentsquare):
        super().__init__(color, currentsquare)
class Bishop:
    def __init__(self, color, currentsquare):
        super().__init__(color, currentsquare)
class Rook:
    def __init__(self, color, currentsquare, moved):
        super().__init__(color, currentsquare)
        self.moved = moved



            
         






pygame.display.flip()




#running section
running = True
while running:

    
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    elif event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        file = pos[0]//60 +1
        rank = pos[1]//60 +1
        square = rank,file
        print(square)

       
       




    
    

        
            

        
