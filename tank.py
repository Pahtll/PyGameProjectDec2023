"""Таня, танчик или просто Т-34."""
import pygame as pg
#from abc import ABC, abstractmethod
#Закоментировал импорт, который пока не пригодился.

class tank():
    """Выпускаем танк со стонка и отправляем на стартовые координаты"""
    def __init__(self, startPos: tuple):
        self.x = startPos[0]
        self.y = startPos[1]

    def move(self, isButtonPressed, direction):
        """Танк перемещается в одном их 4х направлений."""
        # Изменяем координаты по дельте
        while isButtonPressed:
            if direction == pg.K_RIGHT:
                self.x += 10
            elif direction == pg.K_LEFT:
                self.x += -10
            elif direction == pg.K_DOWN:
                self.y += -10
            elif direction == pg.K_UP:
                self.y += 10

    def shot(self) -> None:
        """Т-34 стреляет фугасом."""
        pass

    def die(self) -> None:
        """Скажи, а почему ты вместе с танком не сгорел?"""
        pass

    #Что ещё должен делать танчик?