from random import randrange

class ImageObject:
    def __init__(self,display, x, y, width, image, speed):
        self.x = x
        self.y = y
        self.width = width
        self.image = image
        self.speed = speed
        self.display = display

    def move(self, DISPLAY_WIDHT):
        if self.x >= - self.width:
            self.display.blit(self.image, (self.x, self.y))

            self.x -= self.speed
            return True
        else:
            self.x = DISPLAY_WIDHT+100+randrange(-80, 60)
            return False

    def returnImageObject(self, radius, y, width, image):
        self.x = radius
        self.y = y
        self.width = width
        self.image = image

        self.display.blit(self.image, (self.x, self.y))