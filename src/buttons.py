import pygame


class Buttons: ##sprite
  
  def __init__(self, x, y, image):
    self.image = image
    #pygame.sprite.Sprite.__init__
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y)

  def draw(self):
    screen.blit(self.image, (self.rect.x, self.rect.y))
      
  