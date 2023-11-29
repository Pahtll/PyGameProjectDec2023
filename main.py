import pygame as pg
import tank
import field

pg.init()

# Для упрощения работы в дальнейшем оформил в качестве двух отдельных переменных
width, height = 800, 600
screen = pg.display.set_mode((width, height))
pg.display.set_caption('Чечня 1994')

running = True
while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False

    screen.fill((0, 0, 0))
    pg.display.flip()

pg.quit()