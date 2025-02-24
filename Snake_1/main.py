import pygame

# init pygame
pygame.init

# window dimensions
width = 600
height = 300
screen = pygame.display.set_mode((width,height))

# set window title
pygame.display.set_caption("Snake")

# fps 
clock = pygame.time.Clock()
dt = 0 
speed = 10 

""" Game loop """
runing = True 
while running:
  """Handle events"""
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
  """ Update our game state"""

  """ Draw our screen """
  # Clear screen
  screen.fill("white")

  # Update screen
  pygame.display.flip()

  # FPS
  dt = clock.tick(speed)/1000

# quit game
pygame.quit()  