import pygame as pg
from pygame.sprite import Group
import tank, field, background

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

# Тестовое создание танка
tank1 = tank.Tank()
tank_position = (0, 0)

# Пули от танка
bullets = Group()
# Коробки
boxes = Group()

# Создание поля. Генерация случайного поля, которое будет использоваться до конца игры.
field_of_boxes = field.Field(boxes)
field_of_boxes.generate((10, 30), (1, 10))

running = True
while running:

    # Количество фпс
    clock.tick(FPS)

    # Постоянное отображение заднего фона игры
    screen.blit(background, (0, 0))

    # Создание поля каждый раз по новой
    field_of_boxes.duplicate_screen(screen)

    # Объекту tank1 передаются набор пулек и коробок
    tank1.shot_or_kill_box(bullets, boxes)

    # Отображение спрайта танка
    screen.blit(tank1.surf, tank_position)
    # Объекту tank1 передается список [(x, y), (x1, y1), ...] с содержанием координат коробок
    tank1.get_boxes_coordinates([class_instance.coordinates for class_instance in field_of_boxes.boxes])

    # Нажимаемые клавиши, переменная position для сохранения позиции
    keys_get_pressed = pg.key.get_pressed()
    tank_position = tank1.move(keys_get_pressed)

    # Обновление экрана
    pg.display.update()

    # Передаётся класс tank1 для понимания направления танка и корректировки относительно его направления пуль
    bullets.update(tank1)


    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False
            pg.quit()

        elif event.type == pg.KEYDOWN:
            keyInput = event.key

            if keyInput == pg.K_ESCAPE:
                running = False

            """Пришлось написать управление выстрелом сюда, так как key.get_pressed() 
            реагирует только на удержание кнопки, из-за чего получается ебучий пулемёт.
            К сожалению альтернатрив данному методу, который реагирует только на нажатие я не нашёл
            Кто знает как сделать иначе - делайте."""
            if keyInput == pg.K_SPACE:
                tank1.generate_bullet(screen, bullets)

    # pg.display.flip()

pg.quit()