import pygame as pg
from pygame.sprite import Group
from escape import EscapeMenu
import background, menu, controls, tank, field, animations, hp, save_script

# Запуск программы
pg.init()

# Создание экземпляра класса Clock() для последующего указания количества кадров в секунду
clock = pg.time.Clock()

# Для упрощения работы в дальнейшем оформил в качестве двух отдельных констант
FPS = 60
WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('tanki v tanki')

# Иконка для приложения
icon = pg.image.load('images/tank_topleft/tank1_up.png')
pg.display.set_icon(icon)

# Главное меню
main_menu = menu.MainMenu(screen)


# Установка сложности игры // Оставляйте 1 пока что

def run_game():

    # Задний фон для игры
    background_image = background.create_background()

    # Пули от танка
    bullets_topleft = Group()
    bullets_bottomright = Group()

    # Генерация коробок
    boxes = Group()
    copters = Group()

    # Создание танков
    tank_topleft = tank.TankTopLeft(screen, 0, 0)
    tank_bottomright = tank.TankBottomRight(screen, 764, 558)

    # Создание плашки хп
    hp_topleft = hp.Hp(screen, tank_topleft)
    hp_bottomright = hp.Hp(screen, tank_bottomright)

    tank_topleft(hp_topleft)
    tank_bottomright(hp_bottomright)

    # Создание экземпляра класса взрыв
    explosion = animations.Explosion()

    # Создание поля. Генерация случайного поля, которое будет использоваться до конца игры.
    field_of_boxes = field.Field(boxes)
    field_of_boxes.generate((10, 30), (1, 10))

    # Создание меню с кнопками "продолжить" и "выйти в главное менню"
    escape_menu = EscapeMenu(screen)
    victory_menu = menu.VictoryMenu(screen)

    # Эта переменная отвечает за то, какой кадр будет использоваться в анимации коптера
    copter_image_index = 0
    running = True
    while running:
        # Количество фпс
        clock.tick(FPS)

        controls.set_difficulty(main_menu.difficulty.get_difficulty())

        if not main_menu.is_opened and not main_menu.difficulty.is_opened:

            # Постоянное отображение заднего фона игры
            screen.blit(background_image, (0, 0))

            # Создание поля из коробок каждый раз по новой
            field_of_boxes.duplicate_screen(screen)

            # Объектам tank_topleft и tank_bottomright передаются набор пуль и коробок
            tank_topleft.shot(bullets_topleft, boxes, tank_bottomright, copters, hp_bottomright)
            tank_bottomright.shot(bullets_bottomright, boxes, tank_topleft, copters, hp_topleft)
            tank_topleft.is_alive(explosion)
            tank_bottomright.is_alive(explosion)

            # Отображение спрайта танка
            tank_topleft.update()
            tank_bottomright.update()

            # Отображение плашки на экране
            hp_topleft.update()
            hp_bottomright.update()

            # Объектам tank_topleft и tank_bottomright передается список [(x, y), (x1, y1), ...] с содержанием координат коробок
            tank_topleft.get_boxes_coordinates([class_instance.coordinates for class_instance in field_of_boxes.boxes])
            tank_bottomright.get_boxes_coordinates([class_instance.coordinates for class_instance in field_of_boxes.boxes])

            # Нажимаемые клавиши, переменная position для сохранения позиции
            keys_get_pressed = pg.key.get_pressed()

            for copter_object in copters:

                if copter_image_index > len(copter_object.images) - 1:
                    copter_image_index = 0

                if not escape_menu.is_opened and not victory_menu.is_openned:
                    copter_object.attack(tank_topleft, tank_bottomright)

                else:
                    copter_image_index = 0
                copter_object.die(copters)
                copter_object.draw(copter_image_index)

            if not escape_menu.is_opened:

                victory_menu.draw(tank_topleft, tank_bottomright)
                if not victory_menu.is_openned:
                    """Сюда пишутся все события, которые не должны происходить, когда открывается меню."""
                    # Передаётся класс tank_topleft для понимания направления танка и корректировки относительно его направления пуль
                    bullets_topleft.update(tank_topleft)
                    bullets_bottomright.update(tank_bottomright)

                    # Передвижение танка
                    tank_topleft.move(keys_get_pressed, boxes, tank_bottomright)
                    tank_bottomright.move(keys_get_pressed, boxes, tank_topleft)


        main_menu.draw()
        main_menu.difficulty.draw()

        copter_image_index += 1

        # Отрисовка меню, открываемое на кнопку "esc"
        escape_menu.draw()

        # Обновление экрана
        pg.display.flip()

        for event in pg.event.get():

            if not main_menu.is_opened and not main_menu.difficulty.is_opened:

                escape_menu.open(event, main_menu)
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        tank_topleft.generate_bullet(screen, bullets_topleft, event)
                    if event.key == pg.K_RCTRL:
                        tank_bottomright.generate_bullet(screen, bullets_bottomright, event)

            elif main_menu.is_opened:
                # Если нажата кнопка выхода из игры, то программа должна завершиться.
                main_menu.update(event)

            elif main_menu.difficulty.is_opened:
                main_menu.difficulty.update(event)

            if event.type == pg.QUIT:
                running = False
                pg.quit()

    # Закрываем игру
    pg.quit()
