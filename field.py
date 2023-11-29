"""Случайно генерируемое поле"""
import random
import pygame as pg


class Box:
    """Коробки - это объекты, из которых строится карта """

    def __init__(self, coordinates):
        """Инициализация коробки"""
        self.coordinates = coordinates

    def add(self, screen):
        """Рисует коробку на экране"""
        pg.draw.rect(screen, (255, 255, 255), pg.Rect(*self.coordinates, 50, 50), 2)


def generate(countOfStructures, countOfBoxes, screen):
    """Генерация случайного поля, которое состоит из случайного количества структур.
    Каждая структура состоит из случайного количества коробок, стоящих рядом.
    countOfStructures - отвечает за примерное количество структур
    countOfBoxes - отвечает за примерное количество коробок """

    listOfAllBoxes = set()

    # Первый цикл отвечает за количество структур
    for _ in range(countOfStructures):
        x = random.randrange(0, 800, 50)
        y = random.randrange(0, 600, 50)
        box = Box((x, y))
        listOfAllBoxes.add((x, y))
        box.add(screen)

        # Второй за количество коробок в структуре
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

            # Список, который хранит в себе все данные о коробках. Он понадобится в будущем
            listOfAllBoxes.add((x, y))
            box = Box((x, y))
            box.add(screen)
    print(len(listOfAllBoxes))
