import pygame

class Piece:

    def __init__(self,type,color):

        self.type = type
        self.color = color

        filename = f"images/{color}_{type}.png"

        try:
            img = pygame.image.load(filename)
            self.image = pygame.transform.scale(img,(80,80))
        except:
            self.image = None

    def draw(self,screen,row,col):

        if self.image:
            screen.blit(
                self.image,
                (col*80,row*80)
            )