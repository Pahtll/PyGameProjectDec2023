"""Создание сложности"""
import random

import tank, field, copter

def set_difficulty(range):
    """
    Установка сложности. Уровни сложности:
    1- ничего не меняется
    2 - изменение хп
    3 - изменение хп, скорости танка, пули
    "Test" - для тестеровки при разработке (читерский мод)
    """
    match range:
        case 1:
            tank.Tank.speed = 2
            tank.Tank.hp = 200
            tank.Tank.shot_delay = 500
            tank.Bullet.damage = 50
            tank.Bullet.speed = 10
            field.Box.hp = 150
            field.Box.copter_chance = 0.25 # 25%
            copter.Copter.speed = 1
            copter.Copter.damage = 2
            copter.Copter.hp = 50

        case 2:
            tank.Tank.speed = 2
            tank.Tank.hp = 300
            tank.Tank.shot_delay = 500
            tank.Bullet.damage = 50
            tank.Bullet.speed = 10
            field.Box.hp = 200
            copter.Copter.speed = 2
            copter.Copter.damage = 3
            copter.Copter.hp = 100

        case 3:
            tank.Tank.speed = 2
            tank.Tank.hp = 420
            tank.Tank.shot_delay = 500
            tank.Bullet.damage = 40
            tank.Bullet.speed = 10
            field.Box.hp = 200
            copter.Copter.speed = 3
            copter.Copter.damage = 5
            copter.Copter.hp = 100

        case _:
            tank.Tank.speed = 3
            tank.Tank.hp = 420
            tank.Tank.shot_delay = 0
            tank.Bullet.damage = 500
            tank.Bullet.speed = 20
            field.Box.hp = 40
            copter.Copter.speed = 2
            copter.Copter.damage = 5
            copter.Copter.hp = 100

