"""Создание танка"""
import pygame as pg
import pygame.sprite
import field

class Bullet(pg.sprite.Sprite):
    """Создаём пулю, которая является спрайтом."""

    speed = 5
    damage = 50

    def __init__(self, screen, tank, team):
        """Создаём пулю в позиции танка."""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pg.Rect(tank.rect.centerx, tank.rect.centery, 7, 7)
        self.color = (255, 0, 0)
        #Нужно для того чтобы разграничивать пули одного танка от пуль другого
        self.team = team

        #Направления выстрела = направление танка
        self.direction = tank.direction

        #Координаты центра пули = координатам центра танка
        self.rect.center = tank.rect.center
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self, tank):
        """Перемещение пули. Если танк смотрит вправо, то пуля летит вправо и тд."""

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

    def draw_bullet(self):
        """Отрисовка пули. Пока что пуля это тупо красный шарик."""
        pg.draw.circle(self.screen, self.color, self.rect.center, 7)

class Tank(pg.sprite.Sprite):
    """Выпускаем танк со стонка и отправляем на стартовые координаты"""

    speed = 1
    hp = 200

    def __init__(self, screen, x, y):
        super().__init__()
        self.screen = screen
        self.WIDTH = 20
        self.HEIGHT = 20
        self.rect = self.surf.get_rect()
        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y
        self.boxes_coordinates = []

    def get_boxes_coordinates(self, transferred_boxes_coordinates):
        """Получение координат коробок"""
        self.boxes_coordinates = transferred_boxes_coordinates

    def shot(self, bullets, boxes):
        """
        В первом цикле мы берем по пуле из группы спрайтов пуль. Каждая пуля - экземлпяр класса Bullet().
        Далее отрисовываем каждую пулю.
        Проверяем дошла ли пуля до границы центром. Если да, то убираем её.

        Во втором цикле мы пробегаемся по коробкам из группы спрайтов коробок.
        Проверяем касается ли пуля хитбокса коробки, если касается, то возвращает True.
        """

        for bullet in bullets.sprites():

            # Отрисовываем пулю
            bullet.draw_bullet()

            # Убирает пулю когда она достигает конца экрана
            if bullet.rect.centerx > 800 or bullet.rect.centery > 600 or bullet.rect.centerx < 0 or bullet.rect.centery < 0:
                bullets.remove(bullet)

        # Берём по коробке из группы спрайтов коробок. Для проверки
        for box in boxes.sprites():

            # Если пуля касается хитбокса коробки, то shot = True
            shot = pg.sprite.spritecollide(box, bullets, True)

            if shot:
                # От коробки отнимаем урон от пули
                box.hp -= bullet.damage

                # Удаляем коробку, если она потеряла всем хп
                if box.hp == 0:
                    boxes.remove(box)

    def update(self):
        """Перерисовываем танк на экране."""
        self.screen.blit(self.surf, self.rect)

    def die(self):
        """Скажи, а почему ты вместе с танком не сгорел?"""
        pass

class TankTopLeft(Tank):
    """Отвечает за верхний левый танк (управление на WASD, стрельба не пробел)"""
    def __init__(self, screen, x, y):
        self.surf = pg.image.load('images/tank1.png')
        super().__init__(screen, x, y)

        # direction - направление ствола танка
        self.direction = 'down'

    def move(self, keys, boxes):
        """Танк перемещается в одном их 4х направлений."""

        if keys[pg.K_d]:
            if (self.x < 800 and all((not(x <= self.x + self.WIDTH <= x + 40)) or ((x <= self.x + self.WIDTH <= x + 40)
                and (not(y < self.y + self.HEIGHT < y + 40)) and (not(y < self.y < y + 40)))
                                     for x, y in self.boxes_coordinates)):
                self.x += self.speed
            self.direction = 'right'

        elif keys[pg.K_a]:
            if (self.x > 0 and all((not(x <= self.x <= x + 40)) or ((x <= self.x <= x + 40
                and (not(y < self.y + self.HEIGHT < y + 40))) and (not(y < self.y < y + 40)))
                                     for x, y in self.boxes_coordinates)):
                self.x -= self.speed
            self.direction = 'left'

        elif keys[pg.K_s]:
            if (self.y < 600 and all((not(y <= self.y + self.HEIGHT <= y + 40)) or (y <= self.y + self.HEIGHT <= y + 40
                and (not(x < self.x + self.WIDTH < x + 40)) and (not(x < self.x < x + 40)))
                                     for x, y in self.boxes_coordinates)):
                self.y += self.speed
            self.direction = 'down'

        elif keys[pg.K_w]:
            if (self.y > 0 and all((not(y <= self.y <= y + 40)) or (y <= self.y <= y + 40
                and (not (x < self.x + self.WIDTH < x + 40)) and (not (x < self.x < x + 40)))
                                   for x, y in self.boxes_coordinates)):
                self.y -= self.speed
            self.direction = 'up'

        self.rect.x = self.x
        self.rect.y = self.y

    def generate_bullet(self, screen, bullets, event):
        """
        Каждый раз когда танк стреляет создаётся новая пуля. Пули хранятся в специальном списке со спрайтами.
        Мета-инфа: нельзя сюда впихнуть отрисовку пули bullet.drawBullet(), поскольку она в основном цикле while
        идёт после pg.display.update() (ф-ии выполняющей обновление экрана, для перерисовки его полностью)
        """

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                bullet = Bullet(screen, self, 1)
                bullets.add(bullet)


class TankBottomRight(Tank):
    """Отвечает за нижний правый танк (управление на стрелочки, стрельба на правый контрол."""
    def __init__(self, screen, x, y):
        self.surf = pg.image.load('images/tank2.png')
        super().__init__(screen, x, y)

        # direction - направление ствола танка
        self.direction = 'up'

    def move(self, keys, boxes):
        """Танк перемещается в одном их 4х направлений."""

        if keys[pg.K_RIGHT]:
            if (self.x < 800 and all((not (x <= self.x + self.WIDTH <= x + 40)) or ((x <= self.x + self.WIDTH <= x + 40)
                and (not (y < self.y + self.HEIGHT < y + 40)) and (not (y < self.y < y + 40)))
                                     for x, y in self.boxes_coordinates)):
                self.x += self.speed
            self.direction = 'right'

        elif keys[pg.K_LEFT]:
            if (self.x > 0 and all((not (x <= self.x <= x + 40)) or ((x <= self.x <= x + 40 and
                  (not (y < self.y + self.HEIGHT < y + 40))) and (not (y < self.y < y + 40)))
                                   for x, y in self.boxes_coordinates)):
                self.x -= self.speed
            self.direction = 'left'

        elif keys[pg.K_DOWN]:
            if (self.y < 600 and all((not (y <= self.y + self.HEIGHT <= y + 40)) or (y <= self.y + self.HEIGHT <= y + 40
                    and (not (x < self.x + self.WIDTH < x + 40)) and (not (x < self.x < x + 40)))
                                     for x, y in self.boxes_coordinates)):
                self.y += self.speed
            self.direction = 'down'

        elif keys[pg.K_UP]:
            if (self.y > 0 and all((not (y <= self.y <= y + 40)) or (y <= self.y <= y + 40 and
                (not (x < self.x + self.WIDTH < x + 40)) and (not (x < self.x < x + 40)))
                                   for x, y in self.boxes_coordinates)):
                self.y -= self.speed
            self.direction = 'up'

        self.rect.x = self.x
        self.rect.y = self.y

    def generate_bullet(self, screen, bullets, event):
        """
        Каждый раз когда танк стреляет создаётся новая пуля. Пули хранятся в специальном списке со спрайтами.
        Мета-инфа: нельзя сюда впихнуть отрисовку пули bullet.drawBullet(), поскольку она в основном цикле while
        идёт после pg.display.update() (ф-ии выполняющей обновление экрана, для перерисовки его полностью)
        """

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RCTRL:
                bullet = Bullet(screen, self, 2)
                bullets.add(bullet)
