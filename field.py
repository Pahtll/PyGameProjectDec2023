'''Случайно генерируемое поле'''
import random
import pygame as pg
class Box:

    def __init__(self, coordinates):
        '''Инициализация коробки'''
        self.coordinates = coordinates

    def add(self, screen):
        '''Рисует коробку на экране'''
        pg.draw.rect(screen, (255, 255, 255), pg.Rect(*self.coordinates, 50, 50), 2)

def generate(CountOfBoxes, screen):
    '''Генерация поля'''
    for _ in range(CountOfBoxes):
        box = Box((random.randint(0, 800), random.randint(0, 600)))
        box.add(screen)




