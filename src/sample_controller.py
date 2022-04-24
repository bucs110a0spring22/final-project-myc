
class Controller:
  
  def __init__(self):
    #setup pygame data
    self.display = pygame.set_mode.FULLSCREEN
    self.buttons =src.buttons.Button((500,500),"assets/play_button.png")
    self.STATE = "game"
  def mainloop(self):
    pass
    #select state loop
    
  
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

      #update data

      #redraw
