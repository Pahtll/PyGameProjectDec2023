import pygame as pg
#from abc import ABC, abstractmethod
#Закоментировал импорт, который пока не пригодился.

class tank():
    """Выпускаем танк со стонка и отправляем на стартовые координаты"""
    def __init__(self, startPos: tuple) -> None:
        self.x = startPos[0]
        self.y = startPos[1]
        self.changedX = 0
        self.changedY = 0

    """Танк перемещается в одном их 4х направлений."""
    def move(self, direction: object) -> None:
        if direction == pg.K_RIGHT:
            self.changedX = 10
            self.changedY = 0
        elif direction == pg.K_LEFT:
            self.changedX = -10
            self.changedY = 0
        elif direction == pg.K_DOWN:
            self.changedX = 0
            self.changedY = -10
        elif direction == pg.K_UP:
            self.changedX = 0
            self.changedY = 10
        #Изменяем координаты по дельте
        self.x += self.changedX
        self.y += self.changedY

    def shot(self):
        pass