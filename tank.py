"""Таня, танчик или просто Т-34."""
import pygame as pg
#from abc import ABC, abstractmethod
#Закоментировал импорт, который пока не пригодился.

class tank():
    """Выпускаем танк со стонка и отправляем на стартовые координаты"""
    def __init__(self, startPos: tuple) -> None:
        self.x = startPos[0]
        self.y = startPos[1]

    def move(self, direction: object) -> None:
        """Танк перемещается в одном их 4х направлений."""
        # Изменяем координаты по дельте
        if direction == pg.K_RIGHT:
            self.X += 50
        elif direction == pg.K_LEFT:
            self.X += -50
        elif direction == pg.K_DOWN:
            self.Y += -50
        elif direction == pg.K_UP:
            self.Y += 50

    def shot(self):
        """Т-34 стреляет фугасом."""
        pass

    def die(self):
        """Скажи, а почему ты вместе с танком не сгорел?"""
        pass

    #Что ещё должен делать танчик?