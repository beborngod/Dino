#!/usr/bin/python3

import pygame

class GameBullet:
    def __init__(self,display,x,y,speed=8):
        self.display = display
        self.x = x
        self.y = y
        self.speed = speed
        
    def bulletMove(self, DISPLAY_WIDTH,image):
        self.x+=self.speed
        if self.x<=DISPLAY_WIDTH:
            self.display.blit(image,(self.x,self.y))
            return True
        else:
            return False
