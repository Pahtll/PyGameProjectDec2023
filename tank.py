"""Создание пуль, танков"""
import pygame as pg
import pygame.sprite
import field

class Bullet(pg.sprite.Sprite):
    """Создаём пулю, которая является спрайтом"""

    speed = 5
    damage = 50

    def __init__(self, screen, tank):
        """Создаём пулю в позиции танка"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pg.Rect(tank.rect.centerx, tank.rect.centery, 12, 2)
        self.color = (255, 0, 0)

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

    def draw_bullet(self):
        """Отрисовка пули. Пока что пуля это тупо красный шарик"""
        pg.draw.circle(self.screen, self.color, self.rect.center, 7)

class Tank(pg.sprite.Sprite):
    """Выпускаем танк со стонка и отправляем на стартовые координаты"""

    speed = 1
    hp = 200
    shot_delay = 500

    def __init__(self, screen, x, y):
        super().__init__()
        self.screen = screen
        self.WIDTH = 35
        self.HEIGHT = 39
        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y
        self.boxes_coordinates = []
        # Проверка: жив или нет. По умолчанию стоит True
        self.alive = True

    def get_boxes_coordinates(self, transferred_boxes_coordinates):
        """Получение координат коробок"""
        self.boxes_coordinates = transferred_boxes_coordinates

    def shot(self, bullets, boxes, other_tank):
        """
        В первом цикле мы берем по пуле из группы спрайтов пуль. Каждая пуля - экземлпяр класса Bullet().
        Далее отрисовываем каждую пулю.
        Проверяем дошла ли пуля до границы центром. Если да, то убираем её.

        Во втором цикле мы пробегаемся по коробкам из группы спрайтов коробок.
        Проверяем касается ли пуля хитбокса коробки, если касается, то возвращает True.
        Если
        """

        # Если танк мёртв, то он стрелять больше не может.
        if not(self.alive): return 0

        # Отрисовка по пули и проверка на границы экрана
        for bullet in bullets.sprites():

            # Отрисовываем пулю
            bullet.draw_bullet()

            # Убирает пулю когда она достигает конца экрана
            if bullet.rect.centerx > 800 or bullet.rect.centery > 600 or bullet.rect.centerx < 0 or bullet.rect.centery < 0:
                bullets.remove(bullet)

        # Проверка жив ли чужой танк. Нужно для того, чтобы пули не упирались в его спрайт.
        if other_tank.alive:

            # Проверяет, касается ли пуля другого танка.
            hit = pygame.sprite.spritecollide(other_tank, bullets, True)
            if hit:
                other_tank.hp -= bullet.damage
                if other_tank.hp == 0:
                    other_tank.alive = False

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

class TankTopLeft(Tank):
    """Отвечает за верхний левый танк (управление на WASD, стрельба не пробел)"""

    def __init__(self, screen, x, y):
        self.surf = pg.image.load('images/tank1_down.png')
        self.rect = self.surf.get_rect()

        # Загружаем текстуры для каждого из направлений
        self.image_down = pg.image.load('images/tank1_down.png')
        self.image_right = pg.image.load('images/tank1_right.png')
        self.image_left = pg.image.load('images/tank1_left.png')
        self.image_up = pg.image.load('images/tank1_up.png')

        super().__init__(screen, x, y)
        self.rect.x = self.x
        self.rect.y = self.y

        # direction - направление ствола танка
        self.direction = 'down'

        # last_shot - время последнего выстрела
        self.last_shot = pygame.time.get_ticks() - self.shot_delay

    def move(self, keys, boxes):
        """Танк перемещается в одном их 4х направлений."""

        # Если танк мертв, то двигаться он не может.
        if not (self.alive): return 0

        if keys[pg.K_d]:
            self.direction = 'right'
            if (self.x < 800 and all((not(x <= self.x + self.WIDTH <= x + 40)) or ((x <= self.x + self.WIDTH <= x + 40)
                and (not(y < self.y + self.HEIGHT < y + 40)) and (not(y < self.y < y + 40)))
                                     for x, y in self.boxes_coordinates)):
                self.x += self.speed

        elif keys[pg.K_a]:
            self.direction = 'left'
            if (self.x > 0 and all((not(x <= self.x <= x + 40)) or ((x <= self.x <= x + 40
                and (not(y < self.y + self.HEIGHT < y + 40))) and (not(y < self.y < y + 40)))
                                     for x, y in self.boxes_coordinates)):
                self.x -= self.speed

        elif keys[pg.K_s]:
            self.direction = 'down'
            if (self.y < 600 and all((not(y <= self.y + self.HEIGHT <= y + 40)) or (y <= self.y + self.HEIGHT <= y + 40
                and (not(x < self.x + self.WIDTH < x + 40)) and (not(x < self.x < x + 40)))
                                     for x, y in self.boxes_coordinates)):
                self.y += self.speed

        elif keys[pg.K_w]:
            self.direction = 'up'
            if (self.y > 0 and all((not(y <= self.y <= y + 40)) or (y <= self.y <= y + 40
                and (not (x < self.x + self.WIDTH < x + 40)) and (not (x < self.x < x + 40)))
                                   for x, y in self.boxes_coordinates)):
                self.y -= self.speed

        self.rect.x = self.x
        self.rect.y = self.y

    def generate_bullet(self, screen, bullets_topleft, event):
        """
        Каждый раз когда танк стреляет создаётся новая пуля. Пули хранятся в специальном списке со спрайтами.
        Мета-инфа: нельзя сюда впихнуть отрисовку пули bullet.draw_bullet(), поскольку она в основном цикле while
        идёт после pg.display.update() (ф-ии выполняющей обновление экрана, для перерисовки его полностью)
        """

        # Если танк мертв, то создавать спрайты пуль он не может.
        if not(self.alive): return 0

        now = pygame.time.get_ticks()
        if now - self.last_shot >= self.shot_delay:
            self.last_shot = now
            bullet = Bullet(screen, self)
            bullets_topleft.add(bullet)

    def update(self):
        """Перерисовываем танк на экране."""
        if self.alive:

            if self.direction == 'right':
                self.HEIGHT = 39
                self.WIDTH = 35
                self.screen.blit(self.image_right, self.rect)

            elif self.direction == 'down':
                self.HEIGHT = 35
                self.WIDTH = 39
                self.screen.blit(self.image_down, self.rect)

            elif self.direction == 'left':
                self.HEIGHT = 39
                self.WIDTH = 35
                self.screen.blit(self.image_left, self.rect)

            elif self.direction == 'up':
                self.HEIGHT = 35
                self.WIDTH = 39
                self.screen.blit(self.image_up, self.rect)

class TankBottomRight(Tank):
    """Отвечает за нижний правый танк (управление на стрелочки, стрельба на правый контрол."""
    def __init__(self, screen, x, y):
        self.surf = pg.image.load('images/tank2_right.png')
        self.rect = self.surf.get_rect()

        # Загружаем текстуры танка для каждого направления
        self.image_right = pg.image.load('images/tank2_right.png')
        self.image_left = pg.image.load('images/tank2_left.png')
        self.image_up = pg.image.load('images/tank2_up.png')
        self.image_down = pg.image.load('images/tank2_down.png')

        super().__init__(screen, x, y)
        self.rect.x = self.x
        self.rect.y = self.y

        # direction - направление ствола танка
        self.direction = 'up'

        # last_shot - время последнего выстрела
        self.last_shot = pygame.time.get_ticks() - self.shot_delay

    def move(self, keys, boxes):
        """Танк перемещается в одном их 4х направлений."""

        # Если танк мертв, то двигаться он не может.
        if not (self.alive): return 0

        if keys[pg.K_RIGHT]:
            self.direction = 'right'
            if (self.x < 800 and all((not (x <= self.x + self.WIDTH <= x + 40)) or ((x <= self.x + self.WIDTH <= x + 40)
                and (not (y < self.y + self.HEIGHT < y + 40)) and (not (y < self.y < y + 40)))
                                     for x, y in self.boxes_coordinates)):
                self.x += self.speed

        elif keys[pg.K_LEFT]:
            self.direction = 'left'
            if (self.x > 0 and all((not (x <= self.x <= x + 40)) or ((x <= self.x <= x + 40 and
                  (not (y < self.y + self.HEIGHT < y + 40))) and (not (y < self.y < y + 40)))
                                   for x, y in self.boxes_coordinates)):
                self.x -= self.speed

        elif keys[pg.K_DOWN]:
            self.direction = 'down'
            if (self.y < 600 and all((not (y <= self.y + self.HEIGHT <= y + 40)) or (y <= self.y + self.HEIGHT <= y + 40
                    and (not (x < self.x + self.WIDTH < x + 40)) and (not (x < self.x < x + 40)))
                                     for x, y in self.boxes_coordinates)):
                self.y += self.speed

        elif keys[pg.K_UP]:
            self.direction = 'up'
            if (self.y > 0 and all((not (y <= self.y <= y + 40)) or (y <= self.y <= y + 40 and
                (not (x < self.x + self.WIDTH < x + 40)) and (not (x < self.x < x + 40)))
                                   for x, y in self.boxes_coordinates)):
                self.y -= self.speed

        self.rect.x = self.x
        self.rect.y = self.y

    def generate_bullet(self, screen, bullets_bottomright, event):
        """
        Каждый раз когда танк стреляет создаётся новая пуля. Пули хранятся в специальном списке со спрайтами.
        Мета-инфа: нельзя сюда впихнуть отрисовку пули bullet.drawBullet(), поскольку она в основном цикле while
        идёт после pg.display.update() (ф-ии выполняющей обновление экрана, для перерисовки его полностью)
        """

        # Если танк мертв, то создавать спрайты пуль он не может.
        if not (self.alive): return 0

        now = pygame.time.get_ticks()
        if now - self.last_shot >= self.shot_delay:
            self.last_shot = now
            bullet = Bullet(screen, self)
            bullets_bottomright.add(bullet)

    def update(self):
        """Перерисовываем танк на экране."""
        if self.alive:

            if self.direction == 'right':
                self.screen.blit(self.image_right, self.rect)

            elif self.direction == 'down':
                self.screen.blit(self.image_down, self.rect)

            elif self.direction == 'left':
                self.screen.blit(self.image_left, self.rect)

            elif self.direction == 'up':
                self.screen.blit(self.image_up, self.rect)
