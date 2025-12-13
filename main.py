import pygame
import sys
import time
from datetime import datetime
import os

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Starship')


# Initialize Pygame
pygame.init()
pygame.font.init()
x = 0
y = 0
last_shoot = 2
now = 1

#if this variable is True, then debug mode will be active
debug = True

clock = pygame.time.Clock()
FPS = 60

current_path = os.path.dirname(__file__)
starship_path = os.path.join(current_path, 'sprites', 'starship.png')

try:
    starship_s = pygame.image.load(starship_path).convert_alpha()
except pygame.error as e:
    print(f"Failed to load starship.png: {e}")
    pygame.quit()
    sys.exit()



class player:
    def __init__(self, name, hp, scale, x, y, speed):
        self.name = name
        self.hp = hp
        self.scale = scale
        self.x = x
        self.y = y
        self.speed = speed

    def shooting(self):
        global last_shoot, now
        now = datetime.now()
        last_shoot = (
            now.hour * 3600 +
            now.minute * 60 +
            now.second 
        )
        print(last_shoot)
        print(f"{self.name} attacked")
        colour = (0, 0, 255)
        
        start_x = self.x 
        start_y = self.y + 10
        end_x = self.x 
        end_y = self.y + 400    
        pygame.draw.line(screen, colour , [start_x, start_y], [end_x, end_y])
        
        
    
    def moveA(self):
        self.x -= self.speed
        print(self.x)

    def moveD(self):
        self.x += self.speed
        print(self.x)

        

starship = player("Starship", 100, 10, 0, 0, 5)

#Player visual
player_color = (0,255,0)
player_size=50
starship.x = 400
starship. y = 100



# Load a font
font = pygame.font.SysFont(None, 55)

# Render the text 
text = font.render("DEBUG MODE", True, (255, 255, 255))

# Main game loop

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 
   # Fill the screen with a color (RGB)
    screen.fill((0, 0, 0))
    

    #Attack/Move
    keys = pygame.key.get_pressed()
    now = datetime.now()
    time_now = (
        now.hour * 3600 +
        now.minute * 60 +
        now.second 
    )
    if (time_now - last_shoot) > 0.5:
        if keys[pygame.K_SPACE]:
            starship.shooting() 

    
    if keys[pygame.K_a]:
        starship.moveA()
        #time.sleep(0.25)

    
    if keys[pygame.K_d]:
        starship.moveD()
        #time.sleep(0.5)

    #if the player touches the edge, bounce them back
    while(starship.x + 50 > 800):
        starship.x -= 25
    
    while(starship.x < 0):
        starship.x += 25



  # Blit the text onto the screen
    if debug == True:
        screen.blit(text, (250, 250))

  # Draw player
    colour = (255, 255, 255, 50)
    colour2 = (255, 0, 0, 50)
    pygame.draw.line(screen, colour2, [starship.x, starship.y], [starship.x + 50, starship.y + 50])

    if debug == True:
        pygame.draw.circle(screen, colour, [starship.x, starship.y], 100)
        


  # Update the display
    
    
    #pygame.draw.rect(screen, player_color, (starship.x, starship.y, player_size, player_size))
    screen.blit(starship_s, (starship.x, starship.y))
    pygame.display.flip()

    clock.tick(FPS)