import pygame as pg
from pygame.sprite import Group
import tank, field, background, menu, controls

# Запуск программы
pg.init()

# Создание экземлпяра класса Clock() для последующего указания количества кадров в секунду
clock = pg.time.Clock()

# Для упрощения работы в дальнейшем оформил в качестве двух отдельных констант
FPS = 60
WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('bro, tanki')

# Иконка для приложения
icon = pg.image.load('images/tank1_up.png')
pg.display.set_icon(icon)

#Главное меню
main_menu = menu.MainMenu(screen)

# Задний фон для игры
background = background.create_background()

# Установка сложности игры // Оставляйте 1 пока что
controls.set_difficulty(1)

# Пули от танка
bullets_topleft = Group()
bullets_bottomright = Group()

# Коробки
boxes = Group()

# Создание танков
tank_topleft = tank.TankTopLeft(screen, 0, 0)
tank_bottomright = tank.TankBottomRight(screen, 764, 558)

# Создание поля. Генерация случайного поля, которое будет использоваться до конца игры.
field_of_boxes = field.Field(boxes)
field_of_boxes.generate((10, 30), (1, 10))

# Создание меню с кнопками "продолжить" и "выйти в главное менню"
escape_menu = menu.EscapeMenu(screen)
victory_menu = menu.VictoryMenu(screen)

running = True
while running:
    # Количество фпс
    clock.tick(FPS)

    if main_menu.is_opened == False:
        # Постоянное отображение заднего фона игры
        screen.blit(background, (0, 0))

        # Создание поля из коробок каждый раз по новой
        field_of_boxes.duplicate_screen(screen)

        # Объектам tank_topleft и tank_bottomright передаются набор пуль и коробок
        tank_topleft.shot(bullets_topleft, boxes, tank_bottomright)
        tank_bottomright.shot(bullets_bottomright, boxes, tank_topleft)

        # Отображение спрайта танка
        tank_topleft.update()
        tank_bottomright.update()

        # Объектам tank_topleft и tank_bottomright передается список [(x, y), (x1, y1), ...] с содержанием координат коробок
        tank_topleft.get_boxes_coordinates([class_instance.coordinates for class_instance in field_of_boxes.boxes])
        tank_bottomright.get_boxes_coordinates([class_instance.coordinates for class_instance in field_of_boxes.boxes])

        # Нажимаемые клавиши, переменная position для сохранения позиции
        keys_get_pressed = pg.key.get_pressed()

        # Отрисовка меню, открываемое на кнопку "esc"
        escape_menu.draw()

        if escape_menu.is_opened == False:
            victory_menu.draw(tank_topleft, tank_bottomright)
            if victory_menu.is_openned == False:
                """Сюда пишутся все события, которые не должны происходить, когда открывается меню."""
                # Передаётся класс tank_topleft для понимания направления танка и корректировки относительно его направления пуль
                bullets_topleft.update(tank_topleft)
                bullets_bottomright.update(tank_bottomright)

                # Передвижение танка
                tank_topleft.move(keys_get_pressed, boxes, tank_bottomright)
                tank_bottomright.move(keys_get_pressed, boxes, tank_topleft)

    elif main_menu.is_opened:
        main_menu.draw()

    # Обновление экрана
    pg.display.update()

    for event in pg.event.get():

        if main_menu.is_opened == False:

            escape_menu.open(event, main_menu)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    tank_topleft.generate_bullet(screen, bullets_topleft, event)
                if event.key == pg.K_RCTRL:
                    tank_bottomright.generate_bullet(screen, bullets_bottomright, event)

        elif main_menu.is_opened:
            # Если нажата кнопка выхода из игры, то программа должна завершиться.
            running = main_menu.update(event)

        if event.type == pg.QUIT:
            running = False
            pg.quit()

# Закрываем игру
pg.quit()