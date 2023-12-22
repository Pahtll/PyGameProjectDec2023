"""Создание сложности"""
import random, tank, field, copter, score

def set_difficulty(range):
    """
    Установка сложности. Уровни сложности:
    1 - ничего не меняется
    2 - изменение хп
    3 - изменение хп, скорости танка, пули
    "Test" - для тестировки при разработке (читерский мод)
    """

    chance = 0

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
            chance = 50

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
            chance = 75

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
            chance = 95

    return chance

def set_chance_to_drone(boxes, chance):

    for box in boxes:
        match chance:
            case 50:
                if random.randint(1, 2) == 1:
                    box.is_copter_inside = True
            case 75:
                if random.randint(1, 4) in [1, 2, 3]:
                    box.is_copter_inside = True
            case 95:
                if random.randint(1, 20) in [i for i in range(1, 20)]:
                    box.is_copter_inside = True