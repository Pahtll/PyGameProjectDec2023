'''Случайно генерируемое поле'''
import random
import pygame as pg
class Box:

    def __init__(self, coordinates: tuple) -> None:
        '''Инициализация коробки'''
        self.coordinates = coordinates

    def add(self, screen: tuple) -> None:
        '''Рисует коробку на экране'''
        pg.draw.rect(screen, (255, 255, 255), pg.Rect(*self.coordinates, 50, 50), 2)

def generate(CountOfBoxes: int, screen: tuple) -> None:
    '''Генерация поля'''
    for _ in range(CountOfBoxes):
        box = Box((random.randint(0, 800), random.randint(0, 600)))
        box.add(screen)




