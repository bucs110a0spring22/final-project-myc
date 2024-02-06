import pygame


class Controller:
  
  def __init__(self):
    #setup pygame data
    self.window_width = 500
    self.window_height = 500
    self.STATE = "GAME"
    pygame.init()
    self.display = pygame.display.set_mode((900, 900))
    pygame.display.set_caption('Play Menu')
    #self.buttons =src.buttons.Button((500,500),"assets/play_button.png")
    home_picture = pygame.image.load('assets/baxter.png')
    play_button = pygame.image.load('assets/play_button.png')
  
    #make images into rectangle objects

# draw a green border around img0
  
    self.display.fill((0, 156, 93))
  
    #self.display.blit(home_picture,home_picture_rect)
    self.display.blit(pygame.transform.scale(home_picture, (450,450)), (205, 120))
    self.display.blit(pygame.transform.scale(play_button, (450,450)), (225, 60))

    pygame.display.flip()
    
  
  
  def mainloop(self):
    while self.STATE:
            if self.STATE == "GAME":
                self.gameloop()
            elif self.STATE == "END":
                self.endloop()
    pass
    #select STATE loop
    
  
  ### below are some sample loop states ###

  def menuloop(self):
    while True:
      if self.STATE == "game":
       self.gameloop
      elif self.STATE:
       self.exitloop()
      #event loop

      #update data

      #redraw
      
  def gameloop(self):
      #event loop
    while self.STATE == "game":
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.STATE == 'exit'
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            self.button.reset()
        if event.type == pygame.MOUSEBUTTONDOWN:
          if(self.button.rect.collidepoint(event.pos)):
            self.STATE = 'exit'
      #update data

      #redraw
        self.display.fill(( 0,156,93))
    
  def gameoverloop(self):
      #event loop
     pass
      #update data

      #redraw
