"""Случайно генерируемое поле"""
import random
import pygame as pg

class Field:
    def __init__(self):
        self.boxes = []

    def generate(self, rangeOfStructures, rangeOfBoxes, screen):
        """Генерация случайного поля, которое состоит из случайного количества структур.
        Сначала мы создаём коробку в случайном месте на карте. Затем генерируем случайное число от 1 до 4, которое отвечает
        за позицию следующей коробки относительно предыдущей(если 1, то коробка генерируется справа от предыдущей, если 2
        то снизу и тд). Таким образом мы получаем структуру, состоящую из случайного количества коробок стоящих рядом.
        Коробки не могут появляться по краям экрана
        rangeOfStructures - отвечает за примерное количество структур
        rangeOfBoxes - отвечает за примерное количество коробок."""

        countOfStructures = random.randint(rangeOfStructures[0], rangeOfStructures[1])
        # Первый цикл отвечает за количество структур
        for _ in range(countOfStructures):
            x = random.randrange(40, 760, 40)
            y = random.randrange(40, 560, 40)
            box = Box((x, y))
            self.boxes.append(box)
            countOfBoxes = random.randint(rangeOfBoxes[0], rangeOfBoxes[1])

            # Второй за количество коробок в структуре
            for _ in range(countOfBoxes - 1):
                position = random.randint(1, 4)

                if position == 1 and x + 40 < 760:
                    x += 40

                elif position == 2 and y + 40 < 560:
                    y += 40

                elif position == 3 and x - 40 > 40:
                    x -= 40

                elif position == 4 and y - 40 > 40:
                    y -= 40

                # Список, который хранит в себе все данные о коробках. Он понадобится в будущем
                box = Box((x, y))
                self.boxes.append(box)


    def create(self, screen):
        """
        Функция для перерисовки того же самого поля. Фиксированное поле.
        """
        for box in self.boxes:
            screen.blit(box.texture, box.coordinates)

class Box:
    """Коробки - это объекты, из которых строится карта. Их можно разрушить. Они имеют определённое количество hp. """

    def __init__(self, coordinates):
        """Инициализация коробки"""
        self.coordinates = coordinates
        self.texture = pg.image.load('images/box1.png')
        self.rect = self.texture.get_rect()
        self.boxes = []
        self.hp = 100


