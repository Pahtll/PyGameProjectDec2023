# Создание плашки с хп над танком.
import pygame as pg

class Hp:

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)

    def __init__(self, screen, tank):
        self.screen = screen
        self.tank = tank

        self.width_white_frame = 35
        self.height_white_frame = 10
        self.white_frame = pg.Rect(0, -15, self.width_white_frame, self.height_white_frame)

        self.width_green_line = 31
        self.height_green_line = 6
        self.green_line = pg.Rect(2, -13, self.width_green_line, self.height_green_line)

        self.width_red_line = 0
        self.height_red_line = 6
        self.red_line = pg.Rect(31, -13, self.width_red_line, self.height_red_line)

    def update(self):
        

