import pygame as pg
from abc import ABC, abstractmethod

class tank(ABC):
    """Выпускаем танк со стонка и отправляем на стартовые координаты"""
    def __init__(self, coordinates):
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.changedX = 0
        self.changedY = 0

    """"""
    def move(self, direction):
        if pg.K_RIGHT:
            self.changedX = 10
            changedY = 0
        elif pg.K_LEFT:
            changedX = -10
            changedY = 0
        elif pg.K_DOWN:
            changedX = 0
            changedY = -10
        elif pg.K_UP:
            changedX = 0
            changedY = 10
        self.x += self.changedX
        self.y += self.changedY