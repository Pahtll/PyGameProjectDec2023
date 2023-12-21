"""Создание плашки хп"""
import pygame as pg, tank


class Hp(pg.sprite.Sprite):

    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)

    def __init__(self, screen, tank):
        self.screen = screen
        self.tank = tank

        # Rect(x, y, width, height)
        self.white_frame = pg.Rect(0, 0, 35, 7)
        self.green_line = pg.Rect(0, 0, 33, 5)
        self.red_line = pg.Rect(0, 0, 0, 5)
        # Переменная, которая с каждым выстрелом вычитает выражение round((tank.Tank.hp - self.hp)/33)
        # Разница нынешних хпшек танка от изнчального количества, деленное на 33, потому что 33 - длина в пикселях
        # зеленой полоски
        self.red_line_diff = 35
        self.directional_dependence = {'left': 4, 'right': 0, 'up': 0, 'down': 0}

    def update(self):
        if self.tank.alive:

            self.white_frame.x = self.tank.rect.x + self.directional_dependence[self.tank.direction]
            self.white_frame.y = self.tank.rect.y - 10

            self.green_line.x = self.tank.rect.x + self.directional_dependence[self.tank.direction] + 1
            self.green_line.y = self.tank.rect.y - 9

            self.red_line.x = self.tank.rect.x + self.red_line_diff + self.directional_dependence[self.tank.direction]
            self.red_line.y = self.tank.rect.y - 9

            pg.draw.rect(self.screen, self.WHITE, self.white_frame, 1)
            pg.draw.rect(self.screen, self.GREEN, self.green_line)
            pg.draw.rect(self.screen, self.RED, self.red_line)
        

