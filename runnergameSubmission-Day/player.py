from vector2Dfile import *
import pygame
import random
pygame.init()

print("Imported")


class Player:
    def __init__(self, pos):
        self.pos = pos
        self.vel = Vector(0, 0)
        self.acc = Vector(0, 0)

    def move(self, keyHorizontal, spaceUp, blocks):
        # keyHorizontal == 1 > move right

        if event.key == pygame.K_SPACE:
            if touchesGround:
                self.vel = Vector(0, -10)

        self.acc += Vector(1 * keyHorizontal, 0)
        self.vel += self.acc
        self.pos += self.vel

    def render(self, x, y):


class Block(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.Surface([width, height])
       self.image.fill(color)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()