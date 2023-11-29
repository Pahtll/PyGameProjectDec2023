import pygame as pg
import screeninfo
import Tank



pg.init()
monitor = screeninfo.get_monitors()
width = monitor[0].width
height = monitor[0].height
screen = pg.display.set_mode((width, height))

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