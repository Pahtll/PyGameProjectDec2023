import pygame as pg, tank, pygame.sprite, math

class Copter(pygame.sprite.Sprite):
    """
    Дроны, которые случайно появляются из коробок. Они определяют для себя ближайшую цель и летят к ней.
    Когда хитбокс дрона соприкасается с хитбоксом цели, то у неё постепенно отнимаются хп.
    """
    damage = 0
    speed = 0
    hp = 0

    def __init__(self, screen, x, y):
        super(Copter, self).__init__()
        self.screen = screen
        self.x = x
        self.y = y
        self.rect = pg.Rect(x, y, 30, 30)
        # Список со всеми текстурами который нужен для анимаций.
        self.images = [pg.image.load('images/copter/dronchik.png'), pg.image.load('images/copter/dronchik.png'),
                       pg.image.load('images/copter/dronchik.png'), pg.image.load('images/copter/dronchik.png'),
                       pg.image.load('images/copter/dronchik2.png'), pg.image.load('images/copter/dronchik2.png'),
                       pg.image.load('images/copter/dronchik2.png'), pg.image.load('images/copter/dronchik2.png')]

    def get_nearest_target(self, enemy1, enemy2):
        """
        Метод определяет ближайшую цель и расстояние до неё.
        Возвращает кортеж с экземпляром класса и расстоянием по вектору.
        """

        enemy1_dist = int(
            math.sqrt((enemy1.rect.centerx - self.x) ** 2 + (enemy1.rect.centery - self.y) ** 2))
        enemy2_dist = int(
            math.sqrt((enemy2.rect.centerx - self.x) ** 2 + (enemy2.rect.centery - self.y) ** 2))

        if enemy1_dist >= enemy2_dist:
            target = enemy2
            target_distance = enemy2_dist

        else:
            target = enemy1
            target_distance = enemy1_dist

        return target, target_distance

    def attack(self, enemy1, enemy2):
        """Дрон атакует ближайшую цель"""

        target = self.get_nearest_target(enemy1, enemy2)[0]
        target_distance = self.get_nearest_target(enemy1, enemy2)[1]

        if target_distance != 0:

            if not self.rect.colliderect(target.rect):

                if target.rect.centerx < self.rect.centerx and target.rect.centery < self.rect.centery:

                    self.x -= self.speed * (math.sqrt(2) / 2)
                    self.y -= self.speed * (math.sqrt(2) / 2)

                elif target.rect.centerx > self.rect.centerx and target.rect.centery < self.rect.centery:

                    self.x += self.speed * (math.sqrt(2) / 2)
                    self.y -= self.speed * (math.sqrt(2) / 2)

                elif target.rect.centerx < self.rect.centerx and target.rect.centery > self.rect.centery:

                    self.x -= self.speed * (math.sqrt(2) / 2)
                    self.y += self.speed * (math.sqrt(2) / 2)

                elif target.rect.centerx > self.rect.centerx and target.rect.centery > self.rect.centery:

                    self.x += self.speed * (math.sqrt(2) / 2)
                    self.y += self.speed * (math.sqrt(2) / 2)

                elif target.rect.centerx == self.rect.centerx and target.rect.centery > self.rect.centery:
                    self.y += self.speed

                elif target.rect.centerx == self.rect.centerx and target.rect.centery < self.rect.centery:
                    self.y -= self.speed

                elif target.rect.centerx > self.rect.centerx and target.rect.centery == self.rect.centery:
                    self.x += self.speed

                elif target.rect.centerx < self.rect.centerx and target.rect.centery == self.rect.centery:
                    self.x -= self.speed

                self.rect.x = self.x
                self.rect.y = self.y

            else:
                target.hp -= self.damage
                difference = round((target.hp_line.green_line.width * (1 - (target.hp / tank.Tank.hp))) - target.hp_line.red_line.width)
                target.hp_line.red_line_diff -= difference
                target.hp_line.red_line.width += difference


    def draw(self, image_index):
        self.screen.blit(self.images[image_index], (self.x, self.y))

    def die(self, copters):

        if self.hp <= 0:
            copters.remove(self)
