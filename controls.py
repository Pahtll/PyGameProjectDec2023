"""Создание сложности"""
import tank, field

def set_difficulty(range):
    """
    Установка сложности. Уровни сложности:
    1- ничего не меняется
    2 - изменение хп
    3 - изменение хп, скорости танка, пули
    """
    match range:
        case 1:
            tank.Tank.speed = 1
            tank.Tank.hp = 200
            tank.Tank.shot_delay = 500
            tank.Bullet.damage = 50
            tank.Bullet.speed = 5
            field.Box.hp = 150
        case 2:
            tank.Tank.speed = 2
            tank.Tank.hp = 300
            tank.Tank.shot_delay = 500
            tank.Bullet.damage = 50
            tank.Bullet.speed = 8
            field.Box.hp = 200
        case 3:
            tank.Tank.speed = 3
            tank.Tank.hp = 420
            tank.Tank.shot_delay = 500
            tank.Bullet.damage = 40
            tank.Bullet.speed = 10
            field.Box.hp = 200