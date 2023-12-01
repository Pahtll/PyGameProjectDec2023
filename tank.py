"""Таня, танчик или просто Т-34."""
import pygame as pg
import pygame.sprite
import field
#from abc import ABC, abstractmethod
#Закоментировал импорт, который пока не пригодился.

class Bullet(pg.sprite.Sprite):
    """Создаём пулю, которая является спрайтом"""
    def __init__(self, screen, tank):
        """Создаём пулю в позиции танка"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pg.Rect(tank.rect.centerx, tank.rect.centery, 12, 2)
        self.color = (255, 0, 0)
        self.speed = 5

        #Направления выстрела = направление танка
        self.direction = tank.direction

        #Координаты центра пули = координатам центра танка
        self.rect.center = tank.rect.center
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self, tank):
        """Перемещение пули. Если танк смотрит вправо, то пуля летит вправо и тд"""

        if self.direction == 'right':
            self.x += self.speed

        elif self.direction == 'left':
            self.x -= self.speed

        elif self.direction == 'down':
            self.y += self.speed

        elif self.direction == 'up':
            self.y -= self.speed

        self.rect.x = self.x
        self.rect.y = self.y

    def drawBullet(self):
        """Отрисовка пули. Пока что пуля это тупо красный шарик"""
        pg.draw.circle(self.screen, self.color, self.rect.center, 7)

class Tank(pg.sprite.Sprite):
    """Выпускаем танк со стонка и отправляем на стартовые координаты"""
    def __init__(self):
        super().__init__()
        self.surf = pg.Surface((40, 40))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.x = 0
        self.y = 0
        #direction - направление ствола танка
        self.direction = 'down'
        self.boxes_coordinates = []

    def move(self, keys):
        """Танк перемещается в одном их 4х направлений."""
        # Изменяем координаты по дельте
        if keys[pg.K_d] and self.x < 800 :
            self.x += 1
            self.direction = 'right'

        elif keys[pg.K_a] and self.x > 0:
            self.x -= 1
            self.direction = 'left'

        elif keys[pg.K_s] and self.y < 600:
            self.y += 1
            self.direction = 'down'

        elif keys[pg.K_w] and self.y > 0:
            self.y -= 1
            self.direction = 'up'

        self.rect.x = self.x
        self.rect.y = self.y
        return self.x, self.y

    def get_boxes_coordinates(self, transferred_boxes_coordinates):
        self.boxes_coordinates = transferred_boxes_coordinates

    def shot(self, screen, bullets):
        """каждый раз когда танк стреляет создаётся новая пуля. Пули хранятся в специальном списке со спрайтами."""
        bullet = Bullet(screen, self)
        bullets.add(bullet)

    def die(self):
        """Скажи, а почему ты вместе с танком не сгорел?"""
        pass

    #Что ещё должен делать танчик?

