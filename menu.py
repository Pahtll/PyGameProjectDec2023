"""Здесь прописано меню, которое открывается на клавишу escape"""
import sys
import pygame as pg
import pygame.font
import csv


class Button:
    """
    Кнопка представляет с собой интерактивный объект, на который можно выводить текст
    или взаимодействовать.
    \n screen - экран на котором мы рисуем кнопку.
    \n y - высота кнопки
    \n width - ширина прямоугольника
    \n height - высота прямоугольника
    \n text - текст на кнопке
    """
    def __init__(self, screen, y, width, height, text):
        self.width = width
        self.screen = screen

        # x является константой и равен центру экрана
        self.x = (800 - width) / 2
        self.y = y
        self.rect = pg.Rect(self.x, y, width, height)
        self.height = height
        self.text = text
        self.color = (255, 255, 255)
        self.font = pygame.font.Font(None, int(height / 1.5))
        self.font_color = self.color

        """
        State отвечает за состояние кнопки. Всего есть 3 состояния: 
        normal - обычное, когда ничего не происходит
        hover - когда пользователь наводится на кнопку но не нажимает. 
        pressed - когда пользователь нажал на кнопку
        """
        self.state = 'normal'

    def draw(self):
        """Функция выводит кнопку на экран."""

        pg.draw.rect(self.screen, self.color, self.rect, 10)
        text = self.font.render(self.text, True, self.font_color)
        position = text.get_rect(center=self.rect.center)
        self.screen.blit(text, position)

    def update(self, event):
        """
        Функция update проверяет, совершались ли в этот кадр какие-либо действия с кнопкой. Если совершались,
        то обновляет её состояние.
        """

        if event.type == pg.MOUSEMOTION:

            # Пользователь двинул мышкой и координаты этого движения пришлись на кнопку, то изменить её состояние на hover
            if self.rect.x <= event.pos[0] <= self.rect.topright[0] and self.rect.y <= event.pos[1] <= self.rect.bottomleft[1]:
                self.state = 'hover'

            else:
                self.state = 'normal'

        # Если пользователь навёлся на кнопку, то подсветить её белым
        if self.state == 'hover':
            self.color = (0, 0, 0)

        elif self.state == 'normal':
            self.color = (255, 255, 255)

        # Если пользователь навёлся на кнопку и нажал на мышку, то состояние кнопки - pressed
        if event.type == pg.MOUSEBUTTONDOWN and self.state == 'hover':
            self.state = 'pressed'

        self.font_color = self.color


class MainMenu:
    """Главное меню, из которого происходит вход в игру и выход из неё."""
    def __init__(self, screen):
        self.screen = screen
        self.background = pg.image.load('images/backgrounds/menuBG.png')
        self.button_start = Button(screen, 200, 250, 70, "Начать игру")
        self.button_exit = Button(screen, 300, 250, 70, "Выйти из игры")
        self.is_opened = True

    def draw(self):
        """Отрисовывает меню, состоящее из кнопок и заднего фона """
        if self.is_opened:
            self.screen.blit(self.background, (0, 0))
            self.button_start.draw()
            self.button_exit.draw()

    def update(self, event):
        """Проверка нажаты ли кнопки """
        self.button_start.update(event)
        self.button_exit.update(event)

        if self.button_start.state == 'pressed':
            self.is_opened = False
            self.button_start.state = 'normal'

        elif self.button_exit.state == 'pressed':
            sys.exit()


class VictoryMenu:

    def __init__(self, screen):
        self.screen = screen
        self.is_openned = False
        self.font = pygame.font.Font(None, 100)
        self.font_color = (255, 255, 255)
        self.victories = list()

    def draw(self, tank_topleft, tank_bottom_right):
        with open('saves.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                self.victories = map(int, row)


        if tank_bottom_right.alive == False and tank_topleft.alive == True:

            text = self.font.render(f"Победа Русских!\nТекущий счёт: {self.victories[0]} : {self.victories[1]}", True, self.font_color)
            self.is_openned = True
            if self.is_openned: self.screen.blit(text, (125, 250))

        elif tank_bottom_right.alive == True and tank_topleft.alive == False:

            text = self.font.render(f"Victory of the USA!\nТекущий счёт: {self.victories[0]} : {self.victories[1]}", True, self.font_color)
            self.is_openned = True
            if self.is_openned: self.screen.blit(text, (80, 250))

        elif tank_bottom_right.alive == False and tank_topleft.alive == False:

            text = self.font.render(f"Ничья\nТекущий счёт: {self.victories[0]} : {self.victories[1]}", True, self.font_color)
            self.is_openned = True
            if self.is_openned: self.screen.blit(text, (300, 250))

