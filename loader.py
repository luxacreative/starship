import pygame
import sys
import time
from datetime import datetime
import os

#this is the start of release 1.0           25.12.2025
#this file is made to split the file, global variables and settings loader into a separate file, needed by classes.py

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#loading the ettings
settings = open(r"settings.txt","r+")
settings.seek(0)
first_line = settings.readline().strip()

#if this variable is True, then debug mode will be active
debug = False  
if first_line.startswith("DEBUGMODE="):     #this verifies what the value of DEBUGMODE and set it to debug
    debug = first_line.split("=")[1].lower() == "true"
 
#loading the files
def load():
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

    return starship_s, bullet01_sprite_rotated, bg_s