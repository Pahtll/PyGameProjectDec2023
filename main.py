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

# Задний фон для игры
background = background.create_background()

# Иконка для приложения
icon = pg.image.load('images/icon.png')
pg.display.set_icon(icon)

<<<<<<< Updated upstream
# Тестовое создание танка
tank_object = tank.Tank(screen)
tank_position = (0, 0)

# Установка сложности игры // Оставляйте 1 пока что 
=======
# Установка сложности игры // Оставляйте 1 пока что
>>>>>>> Stashed changes
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

# Создание меню с кнопками "продолжить" и "выйти"
menu = menu.EscapeMenu(screen)

running = True
while running:

    # Количество фпс
    clock.tick(FPS)
    
    # Постоянное отображение заднего фона игры
    screen.blit(background, (0, 0))

    # Создание поля из коробок каждый раз по новой
    field_of_boxes.duplicate_screen(screen)

<<<<<<< Updated upstream
    # Объекту tank1 передаются набор пулек и коробок
    tank_object.shot(bullets, boxes)
=======
    # Объектам tank_topleft и tank_bottomright передаются набор пуль и коробок
    tank_topleft.shot(bullets_topleft, boxes, tank_bottomright)
    tank_bottomright.shot(bullets_bottomright, boxes, tank_topleft)
>>>>>>> Stashed changes

    # Отображение спрайта танка
    tank_object.update()
    # Объекту tank1 передается список [(x, y), (x1, y1), ...] с содержанием координат коробок
    tank_object.get_boxes_coordinates([class_instance.coordinates for class_instance in field_of_boxes.boxes])

    # Нажимаемые клавиши, переменная position для сохранения позиции
    keys_get_pressed = pg.key.get_pressed()
    tank_object.move(keys_get_pressed, boxes)

    # Отрисовка меню, открываемое на кнопку "esc"
    menu.draw()

    # Обновление экрана
    pg.display.update()

<<<<<<< Updated upstream
    # Передаётся класс tank1 для понимания направления танка и корректировки относительно его направления пуль
    bullets.update(tank_object)

    for event in pg.event.get():

=======
    if menu.is_opened == False:
        """Сюда пишутся все события, которые не должны происходить, когда открывается меню."""
        # Передаётся класс tank_topleft для понимания направления танка и корректировки относительно его направления пуль
        bullets_topleft.update(tank_topleft)
        bullets_bottomright.update(tank_bottomright)

        #Передвижение танка
        tank_topleft.move(keys_get_pressed, boxes)
        tank_bottomright.move(keys_get_pressed, boxes)

    for event in pg.event.get():

        if menu.is_opened == False:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    tank_topleft.generate_bullet(screen, bullets_topleft, event)
                if event.key == pg.K_RCTRL:
                    tank_bottomright.generate_bullet(screen, bullets_bottomright, event)

>>>>>>> Stashed changes
        # Открытие меню на esc
        running = menu.open(event)

        if event.type == pg.QUIT:
            running = False
            pg.quit()

        elif event.type == pg.KEYDOWN:
            key_input = event.key

            """Пришлось написать управление выстрелом сюда, так как key.get_pressed() 
            реагирует только на удержание кнопки, из-за чего получается ебучий пулемёт.
            К сожалению альтернатрив данному методу, который реагирует только на нажатие я не нашёл
            Кто знает как сделать иначе - делайте."""
            if key_input == pg.K_SPACE:
                tank_object.generate_bullet(screen, bullets)

pg.quit()