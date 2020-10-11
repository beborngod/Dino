from random import randrange
import pygame

from ImageObgect import ImageObject


pygame.init()


class Dino:
    __DISPLAY_WIDHT = 800
    __DISPLAY_HEIGHT = 600

    __USER_WIDTH = 60
    __USER_HEIGHT = 100

    __cactus_width = 20
    __cactus_height = 70

    __x_cactus = __DISPLAY_WIDHT+50
    __y_cactus = __DISPLAY_HEIGHT-__cactus_height-100

    __USER_X = __DISPLAY_WIDHT//3
    __USER_Y = __DISPLAY_HEIGHT-__USER_HEIGHT-100

    __made_jump = False

    __jump_counter = 30.0
    __clock = pygame.time.Clock()

    __display = pygame.display.set_mode((__DISPLAY_WIDHT, __DISPLAY_HEIGHT))
    pygame.display.set_caption('Dino gonna run!')

    __icon = pygame.image.load('icon.png')
    pygame.display.set_icon(__icon)

    __land = pygame.image.load(r'Land.jpg')

    __cactus_image = [pygame.image.load(
        f'images/Cactus{x}.png') for x in range(3)]

    __stone_image = [pygame.image.load(
        f'images/Stone{x}.png') for x in range(2)]

    __cloud_image = [pygame.image.load(
        f'images/Cloud{x}.png') for x in range(2)]

    __dino_image = [pygame.image.load(f'images/Dino{x}.png') for x in range(5)]

    __cactus_opions = [[69, 449], [73, 410], [40, 420]]

    __image_dinos_counter = 0

    __scores = 0

    __max_scores = 0

    __max_above_cactus_counter = 0

    def getDisplayWidth(self):
        return self.__DISPLAY_WIDHT

    def setDisplayWidth(self, DISPLAY_WIDTH):
        self.__DISPLAY_WIDHT = DISPLAY_WIDTH

    def getDisplayHeight(self):
        return self.__DISPLAY_HEIGHT

    def setDisplayWidth(self, DISPLAY_HEIGHT):
        self.__DISPLAY_HEIGHT = DISPLAY_HEIGHT

    def getUSER_X(self):
        return self.__USER_X

    def setUSER_X(self, USER_X):
        self.__USER_X = USER_X

    def getUSER_Y(self):
        return self.__USER_Y

    def setUSER_Y(self, USER_Y):
        self.__USER_X = USER_Y

    def setLandImage(self, path):
        self.__land.append(pygame.image.load(f'{path}'))

    def setIcon(self, path):
        self.__icon = pygame.image.load(f'{path}')
        pygame.display.set_icon(self.__icon)

    def getDisplaySize(self):
        return [self.__DISPLAY_WIDHT, self.__DISPLAY_HEIGHT]

    def setDisplaySize(self, DISPLAY_WIDTH, DISPLAY_HEIGHT):
        self.__display = pygame.display.set_mode(
            (DISPLAY_WIDTH, DISPLAY_HEIGHT))

    def addDinoImage(self, path):
        self.__dino_image.append(pygame.image.load(f'{path}'))

    def delDinoImage(self, index):
        del self.__dino_image[index]

    def addCactusImage(self, path):
        self.__cactus_image.append(pygame.image.load(f'{path}'))

    def delCactusImage(self, index):
        del self.__cactus_image[index]

    def addCloudeImage(self, path):
        self.__cloud_image.append(pygame.image.load(f'{path}'))

    def delCloudImage(self, index):
        del self.__cloud_image[index]

    def addStoneImage(self, path):
        self.__stone_image.append(pygame.image.load(f'{path}'))

    def delStoneImage(self, index):
        del self.__stone_image[index]

    def main(self):
        self.__game = True
        self.__cactuses = []
        self.createCactus(self.__cactuses)

        self.__stone, self.__cloud = self.openRandomObject(
            self.__stone_image, self.__cloud_image)
        while self.__game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.__made_jump = True

            if self.__made_jump:
                self.jump()

            if keys[pygame.K_ESCAPE]:
                self.pause()

            self.countScores(self.__cactuses)
            self.__display.blit(self.__land, (0, 0))

            self.printText('Scores '+str(self.__scores), 600, 10)

            self.drawCactus(self.__cactuses)
            self.moveImageObjects(self.__stone, self.__cloud)

            self.drawDino()

            if self.checkCollision(self.__cactuses):
                self.__game = False

            pygame.display.update()
            self.__clock.tick(60)

        return self.gameOver()

    def jump(self):
        if self.__jump_counter >= -30.0:
            self.__USER_Y -= self.__jump_counter/2.5
            self.__jump_counter -= 1
        else:
            self.__jump_counter = 30.0
            self.__made_jump = False

    def countScores(self, barriers: list):
        above_cactus = 0
        if -20 <= self.__jump_counter < 25:
            for barrier in barriers:
                #if self.__USER_Y+self.__USER_HEIGHT-5 <= barrier.y:
                if barrier.x <= self.__USER_X <= barrier.x+barrier.width:
                    above_cactus += 1
                elif barrier.x <= self.__USER_X + self.__USER_WIDTH <= barrier.x+barrier.width:
                    above_cactus += 1
    
            self.__max_above_cactus_counter = max(
                self.__max_above_cactus_counter, above_cactus
                )
        else:
            if self.__jump_counter == -30:
                self.__scores += self.__max_above_cactus_counter
                self.__max_above_cactus_counter = 0


    def __makingCactus(self, arr: list, plus_width: int):
        choice = randrange(0, 3)
        image = self.__cactus_image[choice]
        width = self.__cactus_opions[choice][0]
        height = self.__cactus_opions[choice][1]
        arr.append(ImageObject(self.__display,
                               self.__DISPLAY_WIDHT+plus_width, height, width, image, 5))

    def createCactus(self, arr: list):
        self.__makingCactus(arr, 50)
        self.__makingCactus(arr, 300)
        self.__makingCactus(arr, 600)

    def findRadius(self, arr: list):
        radius = int()
        maximum = max(arr[0].x, arr[1].x, arr[2].x)
        if maximum < self.__DISPLAY_WIDHT:
            radius = self.__DISPLAY_WIDHT
            if radius - maximum < 50:
                radius += 280
        else:
            radius = maximum

        choice = randrange(0, 5)
        if choice == 0:
            radius += randrange(10, 15)
        else:
            radius += randrange(250, 400)

        return radius

    def drawCactus(self, arr: list):
        for cactus in arr:
            check = cactus.move(self.__DISPLAY_WIDHT)
            if not check:
                radius = self.findRadius(arr)

                choice = randrange(0, 3)
                image = self.__cactus_image[choice]
                width = self.__cactus_opions[choice][0]
                height = self.__cactus_opions[choice][1]

                cactus.returnImageObject(radius, height, width, image)

    def openRandomObject(self, stone, cloud):
        choice = randrange(0, 2)
        img_stone = self.__stone_image[choice]

        choice = randrange(0, 2)
        img_cloud = self.__cloud_image[choice]

        stone = ImageObject(self.__display, self.__DISPLAY_WIDHT,
                            self.__DISPLAY_HEIGHT-80, 10, img_stone, 4)
        cloud = ImageObject(
            self.__display, self.__DISPLAY_WIDHT, 80, 70, img_cloud, 1)

        return stone, cloud

    def moveImageObjects(self, stone, cloud):
        check = stone.move(self.__DISPLAY_WIDHT)
        if not check:
            choice = randrange(0, 2)
            img_stone = self.__stone_image[choice]
            stone.returnImageObject(
                self.__DISPLAY_WIDHT, 500+randrange(10, 80), stone.width, img_stone)

        check = cloud.move(self.__DISPLAY_WIDHT)
        if not check:
            choice = randrange(0, 2)
            img_cloud = self.__cloud_image[choice]
            cloud.returnImageObject(self.__DISPLAY_WIDHT, randrange(
                10, 200), cloud.width, img_cloud)

    def drawDino(self):
        if self.__image_dinos_counter == 20:
            self.__image_dinos_counter = 0

        self.__display.blit(
            self.__dino_image[self.__image_dinos_counter//4], (self.__USER_X, self.__USER_Y))
        self.__image_dinos_counter += 1

    def printText(self, message, x, y, font_color=(0, 0, 0), font_type='font.ttf', font_size=30):
        font_type = pygame.font.Font(font_type, font_size)
        text = font_type.render(message, True, font_color)
        self.__display.blit(text, (x, y))

    def pause(self):
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.printText('Paused, press Enter to continue!', 160, 200)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                paused = False

            pygame.display.update()
            self.__clock.tick(15)

    def checkCollision(self, barriers: list):
        for barrier in barriers:
            if barrier.y == 449:  # litle cactus
                if not self.__made_jump:  # if Dino not jumping cpllosion
                    if barrier.x <= self.__USER_X+self.__USER_WIDTH-25 <= barrier.x+barrier.width:
                        return True
                elif self.__jump_counter >= 0:  # collision in up
                    if self.__USER_Y+self.__USER_HEIGHT-5 >= barrier.y:
                        if barrier.x <= self.__USER_X+self.__USER_WIDTH-35 <= barrier.x+barrier.width:
                            return True
                else:  # collision in down
                    if self.__USER_Y+self.__USER_HEIGHT-5 >= barrier.y:
                        if barrier.x <= self.__USER_X <= barrier.x+barrier.width:
                            return True

            else:  # a big cactus
                if not self.__made_jump:  # if Dino not jumping cpllosion
                    if barrier.x <= self.__USER_X+self.__USER_WIDTH-5 <= barrier.x+barrier.width:
                        return True
                elif self.__made_jump == 10:  # collision in start jump
                    if self.__USER_Y+self.__USER_HEIGHT-5 >= barrier.y:
                        if barrier.x <= self.__USER_X+self.__USER_WIDTH-5 <= barrier.x+barrier.width:
                            return True
                elif self.__jump_counter <= -1:  # collision in down jump
                    if self.__USER_Y+self.__USER_HEIGHT-15 >= barrier.y:
                        if barrier.x <= self.__USER_X+self.__USER_WIDTH <= barrier.x+barrier.width:
                            return True
                    else:
                        if self.__USER_Y+self.__USER_HEIGHT-10 >= barrier.y:
                            if barrier.x <= self.__USER_X+5 <= barrier.x+barrier.width:
                                return True
        return False

    def gameOver(self):
        stoped = True

        self.__max_scores += self.__scores
        while stoped:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.printText(
                'Game over,go to hell,or press Enter and play again!', 20, 200)
            self.printText(f'You have {self.__max_scores} scores', 270, 100)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                return True
            if keys[pygame.K_ESCAPE]:
                return False

            pygame.display.update()
            self.__clock.tick(15)

    def start(self):
        while self.main():
            self.__scores = 0
            self.__made_jump = False
            self.__jump_counter = 30
            self.__USER_Y = self.__DISPLAY_HEIGHT-self.__USER_HEIGHT-100
        pygame.quit()
        quit()


if __name__ == '__main__':
    game = Dino()
    game.start()
