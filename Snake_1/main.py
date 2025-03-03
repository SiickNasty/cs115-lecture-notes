import pygame
from pygame.constants import KEYDOWN

# init pygame
pygame.init()

# window dimensions
width = 600
height = 400
screen = pygame.display.set_mode((width,height))

# set window title
pygame.display.set_caption("Snake")

# fps 
clock = pygame.time.Clock()
dt = 0 
speed = 10 

# Snake current position
cur_pos = [300,200]
direction = "down"
snake_body = [
  [300,200],
  [300,180],
  [300,160],
  [300,140],
]


""" Game loop """
running = True 
while running:
  """Handle events"""
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    if event.type == KEYDOWN:
        if event.key == pygame.K_ESCAPE: # escape key
            running = False
            
        if event.key == pygame.K_w and direction != "down": # up direction (w)
              direction = "up"
        if event.key == pygame.K_s and direction != "up": # down direction (s)
              direction = "down"
        if event.key == pygame.K_a and direction != "right": # left direction (a)
              direction = "left"
        if event.key == pygame.K_d and direction != "left": # right direction (d)
              direction = "right"

  
  """ Update our game state"""

  #update direction
  if direction == "up":
      cur_pos[1] -= 20
  if direction == "down":
      cur_pos[1] += 20
  if direction == "left":
      cur_pos[0] -= 20
  if direction == "right":
      cur_pos[0] += 20
  
  # boundaries
  if cur_pos[0] < 0: # x-direction boundaries
    cur_pos[0] = 0 
    running = False
  if cur_pos[0] > width-20:  
    cur_pos[0] = width-20
    running = False

  if cur_pos[1] < 0: # y-direction boundaries
    cur_pos[1] = 0
    running = False
  if cur_pos[1] > height-20:
    cur_pos[1] = height-20
    running = False

  # Snake movement
  snake_body.insert(0, list(cur_pos))
  snake_body.pop()

  # Handle lose state 
  
  
  """ Draw our screen """
  # Clear screen
  screen.fill("white")

  # Draw snake
  for body in snake_body: 
    pygame.draw.rect(screen, "black", rect=pygame.Rect(body[0], body[1], 20, 20))
  
  # Update screen
  pygame.display.flip()

  # FPS
  dt = clock.tick(speed)/1000

# quit game
pygame.quit()  