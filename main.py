import pygame as pg
import tank
import field
import random

pg.init()
clock = pg.time.Clock()

# Для упрощения работы в дальнейшем оформил в качестве двух отдельных констант
WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('bro< tanchikiiii')

# Задний фон и иконка
background = pg.image.load("images/background.png")
screen.blit(background, (0, 0))
icon = pg.image.load('images/icon.png')
pg.display.set_icon(icon)

# Тестовое создание танка
tank1 = tank.Tank()
position = (0, 0)


running = True
while running:

    clock.tick(60)

    background = pg.image.load("images/background.png")
    screen.blit(background, (0, 0))

    field.generate((10, 30), (1, 10), screen)

    # Отображение спрайта танка
    screen.blit(tank1.surf, position)

    # Нажимаемые клавиши, переменная position для сохранения позиции
    keys = pg.key.get_pressed()
    position = tank1.move(keys)

    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
        elif event.type == pg.KEYDOWN:
            keyInput = event.key
            if keyInput == pg.K_ESCAPE:
                running = False
                pg.quit()

    # pg.display.flip()

clock.tick(10)

pg.quit()