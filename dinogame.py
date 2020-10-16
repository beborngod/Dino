#!/usr/bin/python3

from random import randrange
import pygame

from ImageObgect import ImageObject
from GameButton import GameButton
from GameBullet import GameBullet


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

    __icon = pygame.image.load('Backgrounds/icon.png')
    pygame.display.set_icon(__icon)

    __fall_sound = pygame.mixer.Sound('Sounds/Bdish.wav')

    __land = pygame.image.load(r'Backgrounds/Land.jpg')

    __cactus_image = [pygame.image.load(
        f'images/Cactus{x}.png') for x in range(3)]

    __stone_image = [pygame.image.load(
        f'images/Stone{x}.png') for x in range(2)]

    __cloud_image = [pygame.image.load(
        f'images/Cloud{x}.png') for x in range(2)]

    __dino_image = [pygame.image.load(f'images/Dino{x}.png') for x in range(5)]
    __dark_dino_image = [pygame.image.load(
        f'images/darkDino{x}.png') for x in range(5)]

    __health_images = pygame.image.load('Effects/heart.png')
    __crash_song = pygame.mixer.Sound('Sounds/loss.wav')
    __new_heart_song = pygame.mixer.Sound('Sounds/hp+.wav')

    __health_images = pygame.transform.scale(__health_images, (30, 30))

    __cactus_opions = [[69, 449], [73, 410], [40, 420]]

    __image_dinos_counter = 0

    __scores = 0

    __max_scores = 0

    __max_above_cactus_counter = 0

    __health = 1

    __button_sound = pygame.mixer.Sound('Sounds/button.wav')

    __switch_character = True

    __bullet_sound = pygame.mixer.Sound('Sounds/shot.wav')
    __bullet_image = pygame.image.load('Effects/shot.png')
    __bullet_image = pygame.transform.scale(__bullet_image, (30, 9))

    __cooldown = 0

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

    def gameMenu(self):
        pygame.mixer.music.load('Sounds/Big_Slinker.ogg')
        pygame.mixer.music.set_volume(30)
        pygame.mixer.music.play(-1)

        actice_color = (23, 254, 56)
        inactive_color = (123, 254, 56)

        menu_background = pygame.image.load('Backgrounds/Menu.jpg')
        show = True

        start_button = GameButton(
            self.__display, 150, 70, actice_color, inactive_color)
        quit_button = GameButton(
            self.__display, 120, 70, actice_color, inactive_color)
        change_personage_button = GameButton(
            self.__display, 240, 70, actice_color, inactive_color)

        while show:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            
            self.__display.blit(menu_background, (0, 0))

            start_button.drawButton(
                320, 200, 'Start', self.__startGame, self.__button_sound, 50)
            change_personage_button.drawButton(
                270, 300, 'Character', self.changeCharacter, self.__button_sound, 50)
            quit_button.drawButton(
                335, 400, 'Quit', quit, self.__button_sound, 50)

            pygame.display.update()
            self.__clock.tick(60)
        

    def changeCharacter(self):
        actice_color = (23, 254, 56)
        inactive_color = (123, 254, 56)

        menu_background = pygame.image.load('Backgrounds/Menu.jpg')
        show = True

        simple_dino_images = pygame.image.load('images/Dino0.png')
        simple_personage_button = GameButton(
            self.__display, 190, 70, actice_color, inactive_color)
        dark_dino_images = pygame.image.load('images/darkDino0.png')
        dark_personage_button = GameButton(
            self.__display, 150, 70, actice_color, inactive_color)

        while show:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.__display.blit(menu_background, (0, 0))

            self.__display.blit(simple_dino_images, (290, 290))
            self.__display.blit(dark_dino_images, (470, 290))

            simple_personage_button.drawButton(
                240, 400, 'Simple ', self.simpleDino, self.__button_sound, 50)

            dark_personage_button.drawButton(
                420, 400, ' Dark', self.darkDino, self.__button_sound, 50)

            pygame.display.update()
            self.__clock.tick(60)

    def simpleDino(self):
        self.__switch_character = True
        self.gameMenu()
        return self.__switch_character

    def darkDino(self):
        self.__switch_character = False
        self.gameMenu()
        return self.__switch_character

    def __startGame(self):  # start game for game menu
        while self.main():
            self.__scores = 0
            self.__made_jump = False
            self.__jump_counter = 30
            self.__USER_Y = self.__DISPLAY_HEIGHT-self.__USER_HEIGHT-100
            self.__health = 1
            self.__cooldown = 0

    def main(self): #------------------------------------------------------------
        pygame.mixer.music.load('Sounds/background.ogg')
        pygame.mixer.music.set_volume(30)
        pygame.mixer.music.play(-1)

        self.game = True
        self.cactuses = []
        self.createCactus(self.cactuses)

        self.stone, self.cloud = self.openRandomObject(
            self.__stone_image, self.__cloud_image
        )

        self.heart = ImageObject(
            self.__display, self.__DISPLAY_WIDHT, 270, 30, self.__health_images, 5)

        all_button_bullets = []

        while self.game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.__made_jump = True

            if self.__made_jump:
                self.jump()

            self.countScores(self.cactuses)
            self.__display.blit(self.__land, (0, 0))

            self.printText('Scores '+str(self.__scores), 600, 10)

            self.drawCactus(self.cactuses)
            self.moveImageObjects(self.stone, self.cloud)

            self.drawDino()
            
            if not self.__cooldown:
                if keys[pygame.K_x]:
                    pygame.mixer.Sound.play(self.__bullet_sound)
                    all_button_bullets.append(GameBullet(self.__display, self.__USER_X+self.__USER_WIDTH-10, self.__USER_Y+30, 10))
                    self.__cooldown = 50
            else:
                self.__cooldown-=1

            for bullet in all_button_bullets:
                if not bullet.bulletMove(self.__DISPLAY_WIDHT,self.__bullet_image):
                    all_button_bullets.remove(bullet)

            if keys[pygame.K_ESCAPE]:
                self.pause()

            self.heart.move(self.__DISPLAY_WIDHT)
            self.heartPlus(self.heart)

            if self.checkCollision(self.cactuses):
                pygame.mixer.music.pause()
                self.game = False
                pygame.mixer.music.load('Sounds/Big_Slinker.ogg')
                pygame.mixer.music.set_volume(30)
                pygame.mixer.music.play(-1)

            self.showHealth()

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
                # if self.__USER_Y+self.__USER_HEIGHT-5 <= barrier.y:
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

    def moveImageObjects(self, stone, cloud):  # drawing stones and clouds
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
        if self.__switch_character == True:
            self.__display.blit(self.__dino_image[self.__image_dinos_counter//4],
                                (self.__USER_X, self.__USER_Y)
                                )
            self.__image_dinos_counter += 1
        if self.__switch_character == False:
            self.__display.blit(self.__dark_dino_image[self.__image_dinos_counter//4],
                                (self.__USER_X, self.__USER_Y)
                                )
            self.__image_dinos_counter += 1

    def printText(self, message, x, y, font_color=(0, 0, 0), font_type='Effects/font.ttf', font_size=30):
        font_type = pygame.font.Font(font_type, font_size)
        text = font_type.render(message, True, font_color)
        self.__display.blit(text, (x, y))

    def pause(self):
        paused = True

        pygame.mixer.music.pause()
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

        pygame.mixer.music.unpause()

    def showHealth(self):
        show = 0
        heart_x = 20
        while show != self.__health:
            self.__display.blit(self.__health_images, (heart_x, 20))
            heart_x += 40
            show += 1

    def checkHealth(self):
        self.__health -= 1
        if self.__health == 0:
            pygame.mixer.Sound.play(self.__crash_song)
            return False
        else:
            pygame.mixer.Sound.play(self.__fall_sound)
            return True

    def __returnObjects(self, arrray, obj):
        radius = self.findRadius(arrray)

        choice = randrange(0, 3)
        image = self.__cactus_image[choice]
        width = self.__cactus_opions[choice][0]
        height = self.__cactus_opions[choice][1]

        obj.returnImageObject(radius, height, width, image)

    def checkCollision(self, barriers: list):
        for barrier in barriers:
            if barrier.y == 449:  # litle cactus
                if not self.__made_jump:  # if Dino not jumping cpllosion
                    if barrier.x <= self.__USER_X+self.__USER_WIDTH-25 <= barrier.x+barrier.width:
                        if self.checkHealth():
                            self.__returnObjects(barriers, barrier)
                            return False
                        else:
                            return True
                elif self.__jump_counter >= 0:  # collision in up
                    if self.__USER_Y+self.__USER_HEIGHT-5 >= barrier.y:
                        if barrier.x <= self.__USER_X+self.__USER_WIDTH-35 <= barrier.x+barrier.width:
                            if self.checkHealth():
                                self.__returnObjects(barriers, barrier)
                                return False
                            else:
                                return True
                else:  # collision in down
                    if self.__USER_Y+self.__USER_HEIGHT-5 >= barrier.y:
                        if barrier.x <= self.__USER_X <= barrier.x+barrier.width:
                            if barrier.x <= self.__USER_X+self.__USER_WIDTH-35 <= barrier.x+barrier.width:
                                if self.checkHealth():
                                    self.__returnObjects(barriers, barrier)
                                    return False
                                else:
                                    return True

            else:  # a big cactus
                if not self.__made_jump:  # if Dino not jumping cpllosion
                    if barrier.x <= self.__USER_X+self.__USER_WIDTH-5 <= barrier.x+barrier.width:
                        if barrier.x <= self.__USER_X+self.__USER_WIDTH-35 <= barrier.x+barrier.width:
                            if self.checkHealth():
                                self.__returnObjects(barriers, barrier)
                                return False
                            else:
                                return True
                elif self.__made_jump == 10:  # collision in start jump
                    if self.__USER_Y+self.__USER_HEIGHT-5 >= barrier.y:
                        if barrier.x <= self.__USER_X+self.__USER_WIDTH-5 <= barrier.x+barrier.width:
                            if barrier.x <= self.__USER_X+self.__USER_WIDTH-35 <= barrier.x+barrier.width:
                                if self.checkHealth():
                                    self.__returnObjects(barriers, barrier)
                                    return False
                                else:
                                    return True
                elif self.__jump_counter <= -1:  # collision in down jump
                    if self.__USER_Y+self.__USER_HEIGHT-15 >= barrier.y:
                        if barrier.x <= self.__USER_X+self.__USER_WIDTH <= barrier.x+barrier.width:
                            if barrier.x <= self.__USER_X+self.__USER_WIDTH-35 <= barrier.x+barrier.width:
                                if self.checkHealth():
                                    self.__returnObjects(barriers, barrier)
                                    return False
                                else:
                                    return True
                else:
                    if self.__USER_Y+self.__USER_HEIGHT-10 >= barrier.y:
                        if barrier.x <= self.__USER_X <= barrier.x+barrier.width:
                            if barrier.x <= self.__USER_X+self.__USER_WIDTH-35 <= barrier.x+barrier.width:
                                if self.checkHealth():
                                    self.__returnObjects(barriers, barrier)
                                    return False
                                else:
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
        self.gameMenu()
        while self.main():
            self.__scores = 0
            self.__made_jump = False
            self.__jump_counter = 30
            self.__USER_Y = self.__DISPLAY_HEIGHT-self.__USER_HEIGHT-100
            self.__health = 1
        pygame.quit()
        quit()

    def heartPlus(self, heart):
        if heart.x <= -heart.width:
            radius = self.__DISPLAY_WIDHT+randrange(2000, 5000)
            heart_y_coord = heart.y+randrange(-15, 40)
            heart.returnImageObject(
                radius, heart_y_coord, heart.width, heart.image)

        if self.__USER_X <= heart.x <= self.__USER_X+self.__USER_WIDTH:
            if self.__USER_Y <= heart.y <= self.__USER_Y+self.__USER_HEIGHT:
                pygame.mixer.Sound.play(self.__new_heart_song)
                if self.__health < 5:
                    self.__health += 1

                radius = self.__DISPLAY_WIDHT+randrange(2000, 5000)
                heart_y_coord = heart.y+randrange(-15, 10)
                heart.returnImageObject(
                    radius, heart_y_coord, heart.width, heart.image)


if __name__ == '__main__':
    game = Dino()
    game.start()
