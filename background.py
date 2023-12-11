"""Создание заднего фона игры"""
import random, pygame as pg


def create_background():
    """Случайная генерация заднего фона."""

    randomNumber = random.randint(0, 10)

    if 5 < randomNumber <= 10:
        background = pg.image.load("images/background2.png")

    elif 0 <= randomNumber <= 5:
        background = pg.image.load("images/background.png")

    return background
