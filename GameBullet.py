#!/usr/bin/python3


class GameBullet:
    def __init__(self, display, x, y, speed=8):
        self.display = display
        self.x = x
        self.y = y
        self.speed = speed
        self.speed_x = 8
        self.speed_y = 0
        self.dest_x = 0
        self.dest_y = 0

    def bulletMove(self, DISPLAY_WIDTH, image):
        self.x += self.speed
        if self.x <= DISPLAY_WIDTH:
            self.display.blit(image, (self.x, self.y))
            return True
        else:
            return False

    def findPath(self, dest_x, dest_y):
        self.dest_x = dest_x
        self.dest_y = dest_y

        delta_x = dest_x - self.x
        count_up = delta_x//self.speed_x

        if self.y >= dest_y:
            delta_y = self.y-dest_y
            self.speed_y = delta_y / count_up
        else:
            delta_y = dest_y - self.y
            self.speed_y = -(delta_y / count_up)

    def moveTo(self, DISPLAY_WIDTH, image,reverse=False):
        if not reverse:
            self.x += self.speed_x
            self.y -= self.speed_y
        else:
            self.x -= self.speed_x
            self.y += self.speed_y

        if self.x <= DISPLAY_WIDTH and not reverse:
            self.display.blit(image, (self.x, self.y))
            return True
        elif self.x>=0 and reverse:
            self.display.blit(image, (self.x, self.y))
            return True
        else:
            return False
