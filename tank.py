"""Таня, танчик или просто Т-34."""
import pygame as pg
#from abc import ABC, abstractmethod
#Закоментировал импорт, который пока не пригодился.

class Tank(pg.sprite.Sprite):
    """Выпускаем танк со стонка и отправляем на стартовые координаты"""
    def __init__(self):
        super().__init__()
        self.surf = pg.Surface((25, 15))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.x = 0
        self.y = 0

    def move(self, keys):
        """Танк перемещается в одном их 4х направлений."""
        # Изменяем координаты по дельте
        if keys[pg.K_d] and self.x < 800:
            self.x += 1
        elif keys[pg.K_a] and self.x > 0:
            self.x -= 1
        elif keys[pg.K_s] and self.y < 600:
            self.y += 1
        elif keys[pg.K_w] and self.y > 0:
            self.y -= 1
        return self.x, self.y

    def shot(self) -> None:
        """Т-34 стреляет фугасом."""
        pass

    def die(self) -> None:
        """Скажи, а почему ты вместе с танком не сгорел?"""
        pass

    #Что ещё должен делать танчик?