"""Таня, танчик или просто Т-34."""
import pygame as pg
#from abc import ABC, abstractmethod
#Закоментировал импорт, который пока не пригодился.

class tank():
    """Выпускаем танк со стонка и отправляем на стартовые координаты"""
    def __init__(self, startPos: tuple) -> None:
        self.x = startPos[0]
        self.y = startPos[1]

    """Танк перемещается в одном их 4х направлений."""
    def move(self, direction: object) -> None:
        # Изменяем координаты по дельте
        if direction == pg.K_RIGHT:
            self.X += 10
            self.Y += 0
        elif direction == pg.K_LEFT:
            self.X += -10
            self.Y += 0
        elif direction == pg.K_DOWN:
            self.X += 0
            self.Y += -10
        elif direction == pg.K_UP:
            self.X += 0
            self.Y += 10


    def shot(self):
        pass