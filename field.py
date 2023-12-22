"""Случайно генерируемое поле"""
import random
import pygame as pg
import pygame.sprite as pgsp

class Box(pgsp.Sprite):
    """Коробки - это объекты, из которых строится карта. Их можно разрушить. Они имеют определённое количество hp."""

    hp = 150

    def __init__(self, coordinates):
        """Инициализация коробки"""
        super().__init__()
        self.coordinates = coordinates
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.texture = pg.image.load('images/boxes/box1.png')
        self.rect = self.texture.get_rect()
        # Передаем два нижних атрибута, чтобы rect понимал размеры коробки и обрабатывал её хитбокс
        self.rect.x = self.coordinates[0]
        self.rect.y = self.coordinates[1]
        self.is_copter_inside = False

class Field:
    """
    Класс Field - поле из коробок.
    Внутри класса есть методы:
    • генерация поля - generate(self, rangeOfStructures, rangeOfBoxes)
    • отрисовка поля на экране - duplicate_screen(screen)

    На входе Field() получает параметр boxes?
    boxes = Group() из pygame.sprite
    """
    def __init__(self, boxes):
        self.boxes = boxes
        self.list_of_coordinates = set()

    def generate(self, range_of_structures, range_of_boxes):
        """
        Генерация случайного поля, которое состоит из случайного количества структур.
        Сначала мы создаём коробку в случайном месте на карте.
        Затем генерируем случайное число от 1 до 4, которое отвечает за позицию следующей коробки
        относительно предыдущей (если 1, то коробка генерируется справа от предыдущей, если 2 то снизу и тд).
        Таким образом мы получаем структуру, состоящую из случайного количества коробок стоящих рядом.
        Коробки не могут появляться по краям экрана.

        * Структуры - это "кучки", "гроздья" коробок, раскиданные по карте.

        Суть параметров:
        • range_of_structures - отвечает за примерное количество структур.
        • range_of_boxes - отвечает за примерное количество коробок в структуре.

        Переменные count_of_structures и count_of_boxes были созданы для дополнительного контроля за рандомностью
        распределения коробок.
        Поскольку range_of_structures и range_of_boxes передают кортежи в виде (x, x`): x < x`, поэтому и
        пишется обращение к индексам в скобках (range_of_structures[0], range_of_structures[1])
        """

        count_of_structures = random.randint(range_of_structures[0], range_of_structures[1])

        # Первый цикл отвечает за количество структур
        for _ in range(count_of_structures):

            x = random.randrange(40, 760, 40)
            y = random.randrange(40, 560, 40)
            while (x, y) in self.list_of_coordinates:
                x = random.randrange(40, 760, 40)
                y = random.randrange(40, 560, 40)

            box = Box((x, y))
            self.boxes.add(box)
            self.list_of_coordinates.add((x, y))

            count_of_boxes = random.randint(range_of_boxes[0], range_of_boxes[1])

            # Второй за количество коробок в структуре
            for _ in range(count_of_boxes - 1):
                position = random.randint(1, 4)

                if position == 1 and x + 40 < 760:
                    x += 40

                elif position == 2 and y + 40 < 560:
                    y += 40

                elif position == 3 and x - 40 > 40:
                    x -= 40

                elif position == 4 and y - 40 > 40:
                    y -= 40

                if (x, y) in self.list_of_coordinates:
                    continue

                # Группа спрайтов, которая хранит в себе все коробки.
                box = Box((x, y))
                self.boxes.add(box)
                self.list_of_coordinates.add((x, y))

    def duplicate_screen(self, screen):
        """Функция для перерисовки того же самого поля. Фиксированное поле."""

        for box in self.boxes.sprites():
            # Передаем в параметры ф-ии текстурку и хитбокс
            # Rect - это прямоугольник, который обозначает границы спрайта
            screen.blit(box.texture, box.rect)
