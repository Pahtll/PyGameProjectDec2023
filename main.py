import pygame as pg
import tank
import field
import random

pg.init()

# Для упрощения работы в дальнейшем оформил в качестве двух отдельных констант
WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('bro< tanchikiiii')

# Задний фон и иконка
randomNumber = random.randint(0, 10)
if randomNumber == 10:
    background = pg.image.load("images/4urka.png")

elif 5 < randomNumber < 10:
    background = pg.image.load("images/background2.png")

elif 0 <= randomNumber <= 5:
    background = pg.image.load("images/background.png")

screen.blit(background, (0, 0))
icon = pg.image.load('images/icon.png')
pg.display.set_icon(icon)

# Тестовое создание танка
tank1 = tank.Tank()
screen.blit(tank1.surf, (0, 0))

field.generate((10, 30), (1, 10), screen)
running = True
while running:

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

    pg.display.flip()

pg.quit()