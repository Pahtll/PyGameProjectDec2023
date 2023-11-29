"""Случайно генерируемое поле"""
import random
import pygame as pg


class Box:

    def __init__(self, coordinates: tuple) -> None:
        """Инициализация коробки"""
        self.coordinates = coordinates

    def add(self, screen: tuple):
        """Рисует коробку на экране"""
        pg.draw.rect(screen, (255, 255, 255), pg.Rect(*self.coordinates, 50, 50), 2)


def generate(countOfBoxes: int, screen: tuple) -> None:
    """Генерация поля"""
    x = random.randint(0, 800)
    y = random.randint(0, 600)
    box = Box((x, y))
    box.add(screen)

    # Цикл генерирует последовательность присоединённых друг к другу коробок в случайном месте карты
    for _ in range(countOfBoxes - 1):
        position = random.randint(1, 4)

        if position == 1 and x + 50 < 800:
            x += 50

        elif position == 2 and y + 50 < 600:
            y += 50

        elif position == 3 and x - 50 > 0:
            x -= 50

        elif position == 4 and y - 50 > 0:
            y -= 50

        box = Box((x, y))
        box.add(screen)