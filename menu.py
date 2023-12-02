"""Здесь прописано меню, которое открываетя на клавишу escape"""
import pygame as pg
import pygame.font


class Button:

    def __init__(self, screen, y, width, height, text):
        self.width = width
        self.screen = screen
        self.x = (800 - width) / 2
        self.y = y
        self.rect = pg.Rect(self.x, y, width, height)
        self.height = height
        self.text = text
        self.color = (0, 0, 0)
        self.font = pygame.font.Font(None, int(height / 1.5))
        self.fontColor = self.color
        self.state = 'normal'

    def draw(self):
        pg.draw.rect(self.screen, self.color, self.rect, 10)
        text = self.font.render(self.text, True, self.fontColor)
        position = text.get_rect(center=self.rect.center)
        self.screen.blit(text, position)

    def update(self, event):

        if event.type == pg.MOUSEMOTION:

            if self.rect.x <= event.pos[0] <= self.rect.topright[0] and self.rect.y <= event.pos[1] <= self.rect.bottomleft[1]:
                self.state = 'hover'

            else:
                self.state = 'normal'

        if self.state == 'hover':
            self.color = (255, 255, 255)

        elif self.state == 'normal':
            self.color = (0, 0, 0)

        if event.type == pg.MOUSEBUTTONDOWN and self.state == 'hover':
            self.state = 'pressed'

        elif event.type == pg.MOUSEBUTTONUP:
            self.state = 'hover'

        self.fontColor = self.color



class EscapeMenu:
    def __init__(self, screen):
        self.screen = screen
        self.buttonResume = Button(screen, 200, 250, 70, "Продолжить")
        self.buttonExit = Button(screen, 300, 250, 70, "Выход")
        self.IsOpened = False

    def draw(self):
        if self.IsOpened:
            self.buttonResume.draw()
            self.buttonExit.draw()

    def open(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self.IsOpened = not self.IsOpened

        if self.IsOpened:
            self.buttonResume.update(event)
            self.buttonExit.update(event)

            if self.buttonExit.state == 'pressed':
                return False
        return True


