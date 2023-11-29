import pygame as pg
import tank


pg.init()
screen_size = 800, 600
screen = pg.display.set_mode(screen_size)
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