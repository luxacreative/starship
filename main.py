import pygame
import sys
import time
from datetime import datetime
import os
import classes
import loader

# Set up the display
pygame.display.set_caption('Starship')

# Initialize Pygame
pygame.init()
pygame.font.init()
loader.load()

starship_s, bullet01_sprite_rotated, bg_s = loader.load()

x = 0
y = 0
last_shoot = 2
now = 1

clock = pygame.time.Clock()
FPS = 60

#define player:
starship = classes.player("Starship", 100, 0, 0, 5, 180)


#Player visual
player_color = (0,255,0)
player_size=50
starship.x = 400
starship.y = 100

# Load a font
font = pygame.font.SysFont(None, 55)

# Prepare the text 
text_surface = font.render("DEBUG MODE", True, (255, 255, 255))
text_surface.set_alpha(128)
text_rotated = pygame.transform.rotate(text_surface, -45)


# Main game loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 
   # Fill the screen with a color (RGB)
    loader.screen.blit(bg_s, (0, 0))

    #Attack/Move
    keys = pygame.key.get_pressed()
    now = datetime.now()
    time_now = (
        now.hour * 3600 +
        now.minute * 60 +
        now.second 
    )

    if keys[pygame.K_SPACE]:
        starship.shooting() 
    
    if keys[pygame.K_a]:
        starship.moveA()

    if keys[pygame.K_d]:
        starship.moveD()

    #if the player touches the edge, bounce them back
    while(starship.x + 50 > 800):
        starship.x -= 25
    
    while(starship.x < 0):
        starship.x += 25

  # Draw the text onto the screen
    if loader.debug == True:
        loader.screen.blit(text_rotated, (250, 250))
  
  # Draw the player

    starship_sprite_rotated = pygame.transform.rotate(starship_s, starship.heading)
    loader.screen.blit(starship_sprite_rotated, (starship.x, starship.y))
    colour = (255, 255, 255)
    colour2 = (255, 0, 0)
    
    if loader.debug == True:
        pygame.draw.line(loader.screen, colour2, [starship.x, starship.y], [starship.x + 50, starship.y + 50])
    else:
        pass
   
  # Update the display
    pygame.display.flip()

    clock.tick(FPS)