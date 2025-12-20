import pygame
import sys
import time
from datetime import datetime
import os

#import loading     #


#loading settings
settings = open(r"settings.txt","r+")
settings.seek(0)
first_line = settings.readline().strip()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Starship')

# Initialize Pygame
pygame.init()
pygame.font.init()

x = 0
y = 0
last_shoot = 2
now = 1

#if this variable is True, then debug mode will be active
debug = False  
if first_line.startswith("DEBUGMODE="):     #this verifies what the value of DEBUGMODE and set it to debug
    debug = first_line.split("=")[1].lower() == "true"
 
clock = pygame.time.Clock()
FPS = 60

current_path = os.path.dirname(__file__)
starship_path = os.path.join(current_path, 'sprites', 'starship.png')
bullet01_path = os.path.join(current_path, 'sprites', '01.png')
bullet11_path = os.path.join(current_path, 'sprites', '11.png')
bg_path = os.path.join(current_path, 'sprites', 'bg.png')

try:
    starship_s = pygame.image.load(starship_path).convert_alpha()
except pygame.error as e:
    print(f"Failed to load starship.png: {e}")
    pygame.quit()
    sys.exit()

try:
    bullet01_s = pygame.image.load(bullet01_path).convert_alpha()
except pygame.error as e:
    print(f"Failed to load 01.png: {e}")
    pygame.quit()
    sys.exit()

try:
    bullet11_s = pygame.image.load(bullet11_path).convert_alpha()
except pygame.error as e:
    print(f"Failed to load 11.png: {e}")
    pygame.quit()
    sys.exit()

try:
    bg_s = pygame.image.load(bg_path).convert_alpha()
except pygame.error as e:
    print(f"Failed to load bg.png: {e}")
    pygame.quit()
    sys.exit()
 
bg_s = pygame.transform.scale(bg_s, (SCREEN_WIDTH, SCREEN_HEIGHT))
bullet01_sprite_rotated = pygame.transform.rotate(bullet01_s, 270)

#class bullet

class bullet:
    def __init__(self, x, y, speed=5):
        self.x = x
        self.y = starship.y +40 
        self.speed = speed

    def update(self):
        start_x = starship.x
        self.y += self.speed
        screen.blit(bullet01_sprite_rotated, (start_x, self.y))  

#class player
class player:
    
    def __init__(self, name, hp, scale, x, y, speed, heading):
        self.name = name
        self.hp = hp
        self.scale = scale
        self.x = x
        self.y = y
        self.speed = speed
        self.heading = heading

    def shooting(self):
        global last_shoot, now
        now = datetime.now()
        last_shoot = (
            now.hour * 3600 +
            now.minute * 60 +
            now.second 
        )

        bullets.append(bullet(self.x + 20, self.y + 40))
        
        colour = (0, 0, 255)
        start_x = self.x 
        start_y = self.y + 10
        end_x = self.x 
        end_y = self.y + 400

        if debug == True:
            print(last_shoot)
            print(f"{self.name} attacked")
            pygame.draw.line(screen, colour , [start_x, start_y], [end_x, end_y])
        bullet.update(self)
        
    def moveA(self):
        self.x -= self.speed
        if debug == True:
            print("x is",self.x)

    def moveD(self):
        self.x += self.speed
        if debug == True:
            print("x is",self.x)

#define player and bullet:
starship = player("Starship", 100, 10, 0, 0, 5, 180)
#bullet01 = bullet("Bullet", 10, 0, 0, 5)

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

bullets = []

# Main game loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 
   # Fill the screen with a color (RGB)
    screen.blit(bg_s, (0, 0))

    #Attack/Move
    keys = pygame.key.get_pressed()
    now = datetime.now()
    time_now = (
        now.hour * 3600 +
        now.minute * 60 +
        now.second 
    )

    #if (time_now - last_shoot) > 0.5:
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
    if debug == True:
        screen.blit(text_rotated, (250, 250))
  
  # Draw the player

    starship_sprite_rotated = pygame.transform.rotate(starship_s, starship.heading)
    screen.blit(starship_sprite_rotated, (starship.x, starship.y))
    colour = (255, 255, 255)
    colour2 = (255, 0, 0)
    
    if debug == True:
        pygame.draw.line(screen, colour2, [starship.x, starship.y], [starship.x + 50, starship.y + 50])
    else:
        pass
   
  # Update the display
    pygame.display.flip()

    clock.tick(FPS)