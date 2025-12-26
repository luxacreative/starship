import pygame
import sys
import time
from datetime import datetime
import os
from . import loader

bullets = []
starship_s, bullet01_sprite_rotated, bg_s = loader.load()

#this is the start of release 1.0           25.12.2025
#this file is made to split the classes into a separate file, independed from main.py

#class bullet

class bullet:
    def __init__(self, x, y, speed=5):
        self.x = 0
        self.y = 0 
        self.speed = speed

    def update(self):   #this function spawns a lot of bullets and move down
        self.y += self.speed    #and the bullets dont get cleared from the screen
        loader.screen.blit(bullet01_sprite_rotated, (self.x, self.y))

#class player
class player:
    
    def __init__(self, name, scale, x, y, speed, heading):
        self.name = name
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

        if loader.debug == True:
            print(last_shoot)
            print(f"{self.name} attacked")
            pygame.draw.line(loader.screen, colour , [start_x, start_y], [end_x, end_y])
        for b in bullets:
            b.update()
        
    def moveA(self):
        self.x -= self.speed
        if loader.debug == True:
            print("x is",self.x)

    def moveD(self):
        self.x += self.speed
        if loader.debug == True:
            print("x is",self.x)

