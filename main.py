import pygame as pg
from pygame.sprite import Group
import tank
import field
import random

pg.init()
clock = pg.time.Clock()

# Для упрощения работы в дальнейшем оформил в качестве двух отдельных констант
FPS = 60
WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('bro, tanki')

# Задний фон и иконка
randomNumber = random.randint(0, 10)

if randomNumber == 10:
    background = pg.image.load("images/4urka.png")

elif 5 < randomNumber < 10:
    background = pg.image.load("images/background2.png")

elif 0 <= randomNumber <= 5:
    background = pg.image.load("images/background.png")

# Иконка
icon = pg.image.load('images/icon.png')
pg.display.set_icon(icon)

# Тестовое создание танка
tank1 = tank.Tank()
position = (0, 0)

# Пули от танка
bullets = Group()

# Создание случайного поля
field1 = field.Field()
field1.generate((10, 30), (1, 10), screen)

running = True
while running:

    clock.tick(FPS)

    background = pg.image.load("images/background.png")
    screen.blit(background, (0, 0))

    for bullet in bullets.sprites():

        bullet.drawBullet()

        #Убирает пулю когда она достигает конца экрана
        if bullet.rect.centerx > 800 or bullet.rect.centery > 600 or bullet.rect.centerx < 0 or bullet.rect.centery < 0:
            bullets.remove(bullet)

    field1.create(screen)

    # Отображение спрайта танка
    screen.blit(tank1.surf, position)
    # Объекту tank1 передается список [(x, y), (x1, y1), ...] с содержанием координат коробок
    tank1.get_boxes_coordinates([class_instance.coordinates for class_instance in field1.boxes])

    # Нажимаемые клавиши, переменная position для сохранения позиции
    keysGetPressed = pg.key.get_pressed()
    keyGetDown = pg.KEYDOWN
    position = tank1.move(keysGetPressed)

    # Обновление экрана
    pg.display.update()

    bullets.update(tank1)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        elif event.type == pg.KEYDOWN:
            keyInput = event.key

            if keyInput == pg.K_ESCAPE:
                running = False

            """Пришлось написать управление выстрелом сюда, так как key.get_pressed() 
            реагирует только на удержание кнопки, из-за чего получается ебучий пулемёт.
            К сожалению альтернатрив данному методу, который реагирует только на нажатие я не нашёл
            Кто знает как сделать иначе - делайте."""
            if keyInput == pg.K_SPACE:
                tank1.shot(screen, bullets)

    # pg.display.flip()

clock.tick(10)

pg.quit()