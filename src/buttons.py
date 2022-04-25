import pygame

class Buttons(pygame.sprite.Sprite): ##sprite
  
  def __init__(self, pos, fn):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load(image)
    self.rect = self.image.get_rect()
    self.rect.x = pos[0]
    self.rect.y = pos[0]

  def draw(self):
    screen.blit(self.image, (self.rect.x, self.rect.y))
      
 