import pygame as pg
import screeninfo
pg.init()

monitor = screeninfo.get_monitors()
width = monitor[0].width
height = monitor[0].height
print(width, height)

screen = pg.display.set_mode((width, height))