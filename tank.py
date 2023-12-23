"""Создание пуль, танков"""
import pygame as pg, pygame.sprite, field, copter, animations, tank

class Bullet(pg.sprite.Sprite):
    """Создаём пулю, которая является спрайтом"""

    speed = 5
    damage = 50

    def __init__(self, screen, tank):
        """Создаём пулю в позиции танка"""
        super(Bullet, self).__init__()
        self.screen = screen
        images = {'right': pg.image.load('images/bullet/bullet_right.png'),
                      'left': pg.image.load('images/bullet/bullet_left.png'),
                      'up': pg.image.load('images/bullet/bullet_up.png'),
                      'down': pg.image.load('images/bullet/bullet_down.png')}
        self.image = images[tank.direction]
        self.rect = self.image.get_rect()
        self.color = (255, 0, 0)

        #Направления выстрела = направление танка
        self.direction = tank.direction

        #Координаты центра пули = координатам центра танка
        self.rect.center = (tank.rect.centerx - 4, tank.rect.centery - 7)
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
        self.screen.blit(self.image, self.rect.center)

class Tank(pg.sprite.Sprite):
    """Выпускаем танк со стонка и отправляем на стартовые координаты"""

    speed = 1
    hp = 560
    shot_delay = 500

    """
    Ниже представлены атрибуты, которые отвечают за кол-во уничтоженных дронов, танков, коробок 
    и попаданий в другой танк. Всё это нужно для подсчёта очков в текущем игровом сеансе.
    """
    killed_drones = 0
    killed_tanks = 0
    killed_boxes = 0
    hit_other_tank = 0

    def __init__(self, screen, x, y):
        super().__init__()
        self.screen = screen
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

    def is_alive(self, explosion):

        if self.hp > 0:
            self.alive = True

        else:
            explosion.boom(self.screen, self.rect.centerx, self.rect.centery)
            self.alive = False

    def __call__(self, hp_line):
        self.hp_line = hp_line

    def shot(self, bullets, boxes, other_tank, copters, hp_other_tank):
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

            for copter_object in copters:
                hit_copter = pygame.sprite.spritecollide(copter_object, bullets, True)

                if hit_copter:
                    copter_object.hp -= bullet.damage
                    if copter_object.hp <= 0:
                        self.killed_drones += 1

            # Проверяет, касается ли пуля другого танка.
            hit_tank = pygame.sprite.spritecollide(other_tank, bullets, True)

            if hit_tank:
                print(other_tank.hp)
                other_tank.hp -= bullet.damage
                self.hit_other_tank += 1
                difference = round((hp_other_tank.green_line.width * (1 - (other_tank.hp / tank.Tank.hp))) - hp_other_tank.red_line.width)
                hp_other_tank.red_line.width += difference
                hp_other_tank.red_line_diff -= difference
                if other_tank.hp <= 0:
                    self.killed_tanks += 1

        # Берём по коробке из группы спрайтов коробок. Для проверки
        for box in boxes.sprites():

            # Если пуля касается хитбокса коробки, то shot = True
            shot = pg.sprite.spritecollide(box, bullets, True)

            if shot:
                # От коробки отнимаем урон от пули
                box.hp -= bullet.damage

                # Удаляем коробку, если она потеряла всем хп
                if box.hp <= 0:
                    boxes.remove(box)
                    self.killed_boxes += 1
                    if box.is_copter_inside:
                        copters.add(copter.Copter(self.screen, box.x, box.y))

class TankTopLeft(Tank):
    """Отвечает за верхний левый танк (управление на WASD, стрельба не пробел)"""

    def __init__(self, screen, x, y):
        self.surf = pg.image.load('images/tank_topleft/tank1_down.png')
        self.rect = self.surf.get_rect()

        # Загружаем текстуры для каждого из направлений
        self.image_down = pg.image.load('images/tank_topleft/tank1_down.png')
        self.image_right = pg.image.load('images/tank_topleft/tank1_right.png')
        self.image_left = pg.image.load('images/tank_topleft/tank1_left.png')
        self.image_up = pg.image.load('images/tank_topleft/tank1_up.png')

        super().__init__(screen, x, y)
        self.rect.x = self.x
        self.rect.y = self.y

        # direction - направление ствола танка
        self.direction = 'down'

        # Размеры танка
        self.WIDTH = 35
        self.HEIGHT = 39

        # last_shot - время последнего выстрела
        self.last_shot = pygame.time.get_ticks() - self.shot_delay

    def move(self, keys, boxes, tank_bottomright):
        """Танк перемещается в одном из 4х направлений."""

        # Если танк мертв, то двигаться он не может.
        if not (self.alive): return 0

        communication_tank = pg.sprite.collide_rect(self, tank_bottomright)

        if keys[pg.K_d]:
            self.direction = 'right'
            self.HEIGHT = 35
            self.WIDTH = 39
            if (self.x < 765 and all((not(x <= self.x + self.WIDTH <= x + 40)) or ((x <= self.x + self.WIDTH <= x + 40)
                and (not(y < self.y + self.HEIGHT < y + 40)) and (not(y < self.y < y + 40)))
                                     for x, y in self.boxes_coordinates) and
                    ((not(tank_bottomright.x <= self.x + self.WIDTH <= tank_bottomright.x + tank_bottomright.WIDTH)) or
                     ((tank_bottomright.x <= self.x + self.WIDTH <= tank_bottomright.x + tank_bottomright.WIDTH) and
                      (not(tank_bottomright.y <= self.y + self.HEIGHT <= tank_bottomright.y + tank_bottomright.HEIGHT))
                      and (not(tank_bottomright.y < self.y < tank_bottomright.y + tank_bottomright.HEIGHT))))):
                self.x += self.speed

        elif keys[pg.K_a]:
            self.direction = 'left'
            self.HEIGHT = 35
            self.WIDTH = 39
            if (self.x > 0 and all((not(x <= self.x <= x + 40)) or ((x <= self.x <= x + 40
                and (not(y < self.y + self.HEIGHT < y + 40))) and (not(y < self.y < y + 40)))
                                     for x, y in self.boxes_coordinates) and
                    ((not(tank_bottomright.x <= self.x <= tank_bottomright.x + tank_bottomright.WIDTH)) or
                     ((tank_bottomright.x <= self.x <= tank_bottomright.x + tank_bottomright.WIDTH) and
                      (not(tank_bottomright.y <= self.y + self.HEIGHT <= tank_bottomright.y + tank_bottomright.HEIGHT))
                      and (not(tank_bottomright.y < self.y < tank_bottomright.y + tank_bottomright.HEIGHT))))):
                self.x -= self.speed

        elif keys[pg.K_s]:
            self.direction = 'down'
            self.HEIGHT = 39
            self.WIDTH = 35
            if (self.y < 565 and all((not(y <= self.y + self.HEIGHT <= y + 40)) or (y <= self.y + self.HEIGHT <= y + 40
                and (not(x < self.x + self.WIDTH < x + 40)) and (not(x < self.x < x + 40)))
                                     for x, y in self.boxes_coordinates) and
                    ((not(tank_bottomright.y <= self.y + self.HEIGHT <= tank_bottomright.y + tank_bottomright.HEIGHT)) or
                     ((tank_bottomright.y <= self.y + self.HEIGHT <= tank_bottomright.y + tank_bottomright.HEIGHT) and
                      (not(tank_bottomright.x <= self.x + self.WIDTH <= tank_bottomright.x + tank_bottomright.WIDTH))
                      and (not(tank_bottomright.x < self.x < tank_bottomright.x + tank_bottomright.WIDTH))))):
                self.y += self.speed

        elif keys[pg.K_w]:
            self.direction = 'up'
            self.HEIGHT = 39
            self.WIDTH = 35
            if (self.y > 0 and all((not(y <= self.y <= y + 40)) or (y <= self.y <= y + 40
                and (not(x < self.x + self.WIDTH < x + 40)) and (not (x < self.x < x + 40)))
                                   for x, y in self.boxes_coordinates) and
                    ((not(tank_bottomright.y <= self.y <= tank_bottomright.y + tank_bottomright.HEIGHT)) or
                     ((tank_bottomright.y <= self.y <= tank_bottomright.y + tank_bottomright.HEIGHT) and
                      (not(tank_bottomright.x <= self.x + self.WIDTH <= tank_bottomright.x + tank_bottomright.WIDTH))
                      and (not(tank_bottomright.x < self.x < tank_bottomright.x + tank_bottomright.WIDTH))))):
                self.y -= self.speed

        self.rect.x = self.x
        self.rect.y = self.y

    def generate_bullet(self, screen, bullets_topleft, event):
        """
        Каждый раз когда танк стреляет, то создаётся новая пуля. Пули хранятся в специальном списке со спрайтами.
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
                self.screen.blit(self.image_right, self.rect)

            elif self.direction == 'down':
                self.screen.blit(self.image_down, self.rect)

            elif self.direction == 'left':
                self.screen.blit(self.image_left, self.rect)

            elif self.direction == 'up':
                self.screen.blit(self.image_up, self.rect)

class TankBottomRight(Tank):
    """Отвечает за нижний правый танк (управление на стрелочки, стрельба на правый контрол.)"""

    def __init__(self, screen, x, y):
        self.surf = pg.image.load('images/tank_bottomright/tank2_right.png')
        self.rect = self.surf.get_rect()

        # Загружаем текстуры танка для каждого направления
        self.image_right = pg.image.load('images/tank_bottomright/tank2_right.png')
        self.image_left = pg.image.load('images/tank_bottomright/tank2_left.png')
        self.image_up = pg.image.load('images/tank_bottomright/tank2_up.png')
        self.image_down = pg.image.load('images/tank_bottomright/tank2_down.png')

        super().__init__(screen, x, y)
        self.rect.x = self.x
        self.rect.y = self.y

        # direction - направление ствола танка
        self.direction = 'up'

        # Размеры танка
        self.WIDTH = 35
        self.HEIGHT = 39

        # last_shot - время последнего выстрела
        self.last_shot = pygame.time.get_ticks() - self.shot_delay

    def move(self, keys, boxes, tank_topleft):
        """Танк перемещается в одном их 4х направлений."""

        # Если танк мертв, то двигаться он не может.
        if not (self.alive): return 0

        if keys[pg.K_RIGHT]:
            self.direction = 'right'
            self.HEIGHT = 35
            self.WIDTH = 39
            if (self.x < 765 and all((not (x <= self.x + self.WIDTH <= x + 40)) or ((x <= self.x + self.WIDTH <= x + 40)
                and (not (y < self.y + self.HEIGHT < y + 40)) and (not (y < self.y < y + 40)))
                                     for x, y in self.boxes_coordinates) and
                    ((not(tank_topleft.x <= self.x + self.WIDTH <= tank_topleft.x + tank_topleft.WIDTH)) or
                     ((tank_topleft.x <= self.x + self.WIDTH <= tank_topleft.x + tank_topleft.WIDTH) and
                      (not(tank_topleft.y <= self.y + self.HEIGHT <= tank_topleft.y + tank_topleft.HEIGHT))
                      and (not(tank_topleft.y < self.y < tank_topleft.y + tank_topleft.HEIGHT))))):
                self.x += self.speed

        elif keys[pg.K_LEFT]:
            self.direction = 'left'
            self.HEIGHT = 35
            self.WIDTH = 39
            if (self.x > 0 and all((not (x <= self.x <= x + 40)) or ((x <= self.x <= x + 40 and
                  (not (y < self.y + self.HEIGHT < y + 40))) and (not (y < self.y < y + 40)))
                                   for x, y in self.boxes_coordinates) and
                    ((not(tank_topleft.x <= self.x <= tank_topleft.x + tank_topleft.WIDTH)) or
                     ((tank_topleft.x <= self.x <= tank_topleft.x + tank_topleft.WIDTH) and
                      (not(tank_topleft.y <= self.y + self.HEIGHT <= tank_topleft.y + tank_topleft.HEIGHT))
                      and (not(tank_topleft.y < self.y < tank_topleft.y + tank_topleft.HEIGHT))))):
                self.x -= self.speed

        elif keys[pg.K_DOWN]:
            self.direction = 'down'
            self.HEIGHT = 39
            self.WIDTH = 35
            if (self.y < 565 and all((not (y <= self.y + self.HEIGHT <= y + 40)) or (y <= self.y + self.HEIGHT <= y + 40
                    and (not (x < self.x + self.WIDTH < x + 40)) and (not (x < self.x < x + 40)))
                                     for x, y in self.boxes_coordinates) and
                    ((not(tank_topleft.y <= self.y + self.HEIGHT <= tank_topleft.y + tank_topleft.HEIGHT)) or
                     ((tank_topleft.y <= self.y + self.HEIGHT <= tank_topleft.y + tank_topleft.HEIGHT) and
                      (not(tank_topleft.x <= self.x + self.WIDTH <= tank_topleft.x + tank_topleft.WIDTH))
                      and (not(tank_topleft.x < self.x < tank_topleft.x + tank_topleft.WIDTH))))):
                self.y += self.speed

        elif keys[pg.K_UP]:
            self.direction = 'up'
            self.HEIGHT = 39
            self.WIDTH = 35
            if (self.y > 0 and all((not (y <= self.y <= y + 40)) or (y <= self.y <= y + 40 and
                (not (x < self.x + self.WIDTH < x + 40)) and (not (x < self.x < x + 40)))
                                   for x, y in self.boxes_coordinates) and
                    ((not(tank_topleft.y <= self.y <= tank_topleft.y + tank_topleft.HEIGHT)) or
                     ((tank_topleft.y <= self.y <= tank_topleft.y + tank_topleft.HEIGHT) and
                      (not(tank_topleft.x <= self.x + self.WIDTH <= tank_topleft.x + tank_topleft.WIDTH))
                      and (not(tank_topleft.x < self.x < tank_topleft.x + tank_topleft.WIDTH))))):
                self.y -= self.speed

        self.rect.x = self.x
        self.rect.y = self.y

    def generate_bullet(self, screen, bullets_bottomright, event):
        """
        Каждый раз когда танк стреляет, то создаётся новая пуля. Пули хранятся в специальном списке со спрайтами.
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