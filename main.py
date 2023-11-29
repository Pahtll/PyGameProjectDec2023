import pygame as pg
import tank
import field

pg.init()

# Для упрощения работы в дальнейшем оформил в качестве двух отдельных констант
tank1 = tank((0, 0))#Тестовый танк заглушка
WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Чечня 1994')
screen.fill((0, 0, 0))
field.generate(20, screen)
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            keyInput = event.key
            if keyInput == pg.K_ESCAPE:
                running = False
            else:
                tank1.move(keyInput)


    pg.display.flip()

pg.quit()