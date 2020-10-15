import pygame


class GameButton:
    def __init__(self,display, width, height, inactive_color, active_color):
        self.display = display
        self.width = width
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color

    def __printText(self, message, x, y, font_color=(0, 0, 0), font_type='Effects/font.ttf', font_size=30):
        font_type = pygame.font.Font(font_type, font_size)
        text = font_type.render(message, True, font_color)
        self.display.blit(text, (x, y))

    def drawButton(self, x, y, message: str, action=None,button_sound=None,font_size=30):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x+self.width and y < mouse[1] < y+self.height:
                pygame.draw.rect(self.display,self.active_color,(x,y,self.width,self.height))
                if click[0] == 1:
                    pygame.mixer.Sound.play(button_sound)
                    pygame.time.delay(300)
                    if action is not None:
                        if action == quit:
                            pygame.quit()
                        action()
                    
        else:
            pygame.draw.rect(self.display,self.inactive_color,(x,y,self.width,self.height))

        self.__printText(message=message,x=x+10,y=y+10,font_size=font_size)