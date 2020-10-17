#!/usr/bin/python3

from random import randrange


class GameBird:
    def __init__(self, display, away_y, image):
        self.display = display
        self.x = randrange(550, 740)
        self.y = away_y
        self.away_y = away_y
        self.image = image
        self.width = 105
        self.height = 55
        self.speed = 4
        self.dest_y = self.speed + randrange(20, 300)
        self.image_count = 0
        self.cooldown_hide = 0
        self.come = True
        self.go_away = False

    def draw(self):
        if self.image_count == 30:
            self.image_count = 0

        self.display.blit(self.image[self.image_count//5], (self.x, self.y))
        self.image_count += 1

        if self.come and self.cooldown_hide == 0:
            return 1

        elif self.go_away:
            return 2

        elif self.cooldown_hide > 0:
            self.cooldown_hide -= 1

        return 0

    def comeBird(self):
        if self.y < self.dest_y:
            self.y += self.speed
        else:
            self.come = False
            self.go_away = True
            self.dest_y = self.away_y

    def hide(self):
        if self.y > self.dest_y:
            self.y -= self.speed
        else:
            self.come = True
            self.go_away = False
            self.x = randrange(550, 740)
            self.dest_y = self.speed + randrange(20, 300)
            self.cooldown_hide = 100

    def checkDamage(self, bullet):
        if self.x <= bullet.x <= self.x+self.width:
            if self.y <= bullet.y <= self.y+self.height:
                self.y=-100
                return True