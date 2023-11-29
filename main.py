import pygame as pg
import screeninfo
pg.init()

monitor = screeninfo.get_monitors()
width = monitor[0].width
height = monitor[0].height
print(width, height)

screen = pg.display.set_mode((width, height))

running = True
while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((255, 255, 255))

    pg.display.flip()

pg.quit()