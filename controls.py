"""Создание сложности"""
import random, tank, field, copter, score

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
            tank.Tank.hp = 250
            tank.Tank.shot_delay = 500
            tank.Bullet.damage = 50
            tank.Bullet.speed = 10
            field.Box.hp = 150
            copter.Copter.speed = 1
            copter.Copter.damage = 2
            copter.Copter.hp = 50
            score.kill_box_coefficient = 0
            score.hit_tank_coefficient = 1
            score.kill_drone_coefficient = 1
            score.kill_tank_coefficient = 5

        case 2:
            tank.Tank.speed = 2
            tank.Tank.hp = 350
            tank.Tank.shot_delay = 500
            tank.Bullet.damage = 50
            tank.Bullet.speed = 10
            field.Box.hp = 200
            copter.Copter.speed = 2
            copter.Copter.damage = 3
            copter.Copter.hp = 100
            score.kill_box_coefficient = 1
            score.hit_tank_coefficient = 2
            score.kill_drone_coefficient = 2
            score.kill_tank_coefficient = 14

        case 3:
            tank.Tank.speed = 2
            tank.Tank.hp = 320
            tank.Tank.shot_delay = 500
            tank.Bullet.damage = 40
            tank.Bullet.speed = 10
            field.Box.hp = 200
            copter.Copter.speed = 3
            copter.Copter.damage = 5
            copter.Copter.hp = 100
            score.kill_box_coefficient = 1
            score.hit_tank_coefficient = 3
            score.kill_drone_coefficient = 3
            score.kill_tank_coefficient = 24

        case _:
            tank.Tank.speed = 5
            tank.Tank.hp = 300
            tank.Tank.shot_delay = 0
            tank.Bullet.damage = 70
            tank.Bullet.speed = 20
            field.Box.hp = 40
            copter.Copter.speed = 2
            copter.Copter.damage = 5
            copter.Copter.hp = 100
            score.kill_tank_coefficient = 24
