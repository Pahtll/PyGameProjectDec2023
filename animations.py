import pygame as pg

class Explosion:
    """В этом классе описан объект взрыв, который происходит при смерти танка"""

    def __init__(self):
        # Текущий кадр
        self.frame_index = 0
        # Кадры взрыва
        self.frames = [pg.image.load('images/animations/explosion/frame_00_delay-0.05s.png'),
                      pg.image.load('images/animations/explosion/frame_00_delay-0.05s.png'),

                      pg.image.load('images/animations/explosion/frame_01_delay-0.05s.png'),
                      pg.image.load('images/animations/explosion/frame_01_delay-0.05s.png'),

                      pg.image.load('images/animations/explosion/frame_02_delay-0.05s.png'),
                      pg.image.load('images/animations/explosion/frame_02_delay-0.05s.png'),

                      pg.image.load('images/animations/explosion/frame_03_delay-0.05s.png'),
                      pg.image.load('images/animations/explosion/frame_03_delay-0.05s.png'),

                      pg.image.load('images/animations/explosion/frame_04_delay-0.05s.png'),
                      pg.image.load('images/animations/explosion/frame_04_delay-0.05s.png'),

                      pg.image.load('images/animations/explosion/frame_05_delay-0.05s.png'),
                      pg.image.load('images/animations/explosion/frame_05_delay-0.05s.png'),

                      pg.image.load('images/animations/explosion/frame_06_delay-0.05s.png'),
                      pg.image.load('images/animations/explosion/frame_06_delay-0.05s.png'),

                      pg.image.load('images/animations/explosion/frame_07_delay-0.05s.png'),
                      pg.image.load('images/animations/explosion/frame_07_delay-0.05s.png'),

                      pg.image.load('images/animations/explosion/frame_08_delay-0.05s.png'),
                      pg.image.load('images/animations/explosion/frame_08_delay-0.05s.png'),

                      pg.image.load('images/animations/explosion/frame_09_delay-0.05s.png'),
                      pg.image.load('images/animations/explosion/frame_09_delay-0.05s.png'),

                      pg.image.load('images/animations/explosion/frame_10_delay-0.05s.png'),
                      pg.image.load('images/animations/explosion/frame_10_delay-0.05s.png'),

                      pg.image.load('images/animations/explosion/frame_11_delay-0.05s.png'),
                      pg.image.load('images/animations/explosion/frame_11_delay-0.05s.png'),

                      pg.image.load('images/animations/explosion/frame_12_delay-0.05s.png'),
                      pg.image.load('images/animations/explosion/frame_12_delay-0.05s.png'),

                      pg.image.load('images/animations/explosion/frame_13_delay-0.05s.png'),
                      pg.image.load('images/animations/explosion/frame_13_delay-0.05s.png'),

                      pg.image.load('images/animations/explosion/frame_14_delay-0.05s.png'),
                      pg.image.load('images/animations/explosion/frame_14_delay-0.05s.png'),

                      pg.image.load('images/animations/explosion/frame_15_delay-0.05s.png'),
                      pg.image.load('images/animations/explosion/frame_15_delay-0.05s.png'),

                      pg.image.load('images/animations/explosion/frame_16_delay-0.05s.png'),
                      pg.image.load('images/animations/explosion/frame_16_delay-0.05s.png'),

                      pg.image.load('images/animations/explosion/frame_17_delay-0.05s.png'),
                      pg.image.load('images/animations/explosion/frame_17_delay-0.05s.png'),

                      pg.image.load('images/animations/explosion/frame_18_delay-0.05s.png'),
                      pg.image.load('images/animations/explosion/frame_18_delay-0.05s.png'),

                      pg.image.load('images/animations/explosion/frame_19_delay-0.05s.png'),
                      pg.image.load('images/animations/explosion/frame_19_delay-0.05s.png'),

                      pg.image.load('images/animations/explosion/frame_20_delay-0.05s.png'),
                      pg.image.load('images/animations/explosion/frame_20_delay-0.05s.png'),

                      pg.image.load('images/animations/explosion/frame_21_delay-0.05s.png'),
                      pg.image.load('images/animations/explosion/frame_21_delay-0.05s.png'),

                      pg.image.load('images/animations/explosion/frame_22_delay-0.05s.png'),
                      pg.image.load('images/animations/explosion/frame_22_delay-0.05s.png'),

                      pg.image.load('images/animations/explosion/frame_23_delay-0.05s.png'),
                      pg.image.load('images/animations/explosion/frame_23_delay-0.05s.png'),

                      pg.image.load('images/animations/explosion/frame_24_delay-0.05s.png'),
                      pg.image.load('images/animations/explosion/frame_24_delay-0.05s.png'),

                      pg.image.load('images/animations/explosion/frame_25_delay-0.05s.png'),
                      pg.image.load('images/animations/explosion/frame_25_delay-0.05s.png'),

                      pg.image.load('images/animations/explosion/frame_26_delay-0.05s.png'),
                      pg.image.load('images/animations/explosion/frame_26_delay-0.05s.png'),

                      pg.image.load('images/animations/explosion/frame_27_delay-0.05s.png'),
                      pg.image.load('images/animations/explosion/frame_27_delay-0.05s.png'),

                      pg.image.load('images/animations/explosion/frame_28_delay-0.05s.png'),
                      pg.image.load('images/animations/explosion/frame_28_delay-0.05s.png'),

                      pg.image.load('images/animations/explosion/frame_29_delay-0.05s.png'),
                      pg.image.load('images/animations/explosion/frame_29_delay-0.05s.png'),

                      pg.image.load('images/animations/explosion/frame_30_delay-0.05s.png'),
                      pg.image.load('images/animations/explosion/frame_30_delay-0.05s.png'),

                      pg.image.load('images/animations/explosion/frame_31_delay-0.05s.png'),
                      pg.image.load('images/animations/explosion/frame_31_delay-0.05s.png'),

                      pg.image.load('images/animations/explosion/frame_32_delay-0.05s.png'),
                      pg.image.load('images/animations/explosion/frame_32_delay-0.05s.png')]

    def boom(self, screen, x, y):
        """Метод boom вызывает анимацию взрыва"""

        if self.frame_index != len(self.frames):
            screen.blit(self.frames[self.frame_index], (x - 30, y - 30))
            self.frame_index += 1
