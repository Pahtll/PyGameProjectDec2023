import tank, field

def set_difficulty(range):
    match range:
        case 1:
            tank.Tank.speed = 1
            tank.Tank.hp = 200
            tank.Tank.shot_delay = 500
            tank.Bullet.damage = 50
            tank.Bullet.speed = 5
            field.Box.hp = 150
        case 2:
            tank.Tank.speed = 1
            tank.Tank.hp = 300
            tank.Tank.shot_delay = 500
            tank.Bullet.damage = 50
            tank.Bullet.speed = 5
            field.Box.hp = 200
        case 3:
            tank.Tank.speed = 3
            tank.Tank.hp = 420
            tank.Tank.shot_delay = 500
            tank.Bullet.damage = 40
            tank.Bullet.speed = 8
            field.Box.hp = 200