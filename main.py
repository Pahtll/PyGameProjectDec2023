import pygame as pg
from pygame.sprite import Group
import tank, field, background, menu

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
tank_object = tank.Tank(screen)
tank_position = (0, 0)

# Пули от танка
bullets = Group()
# Коробки
boxes = Group()

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

    # Объекту tank1 передаются набор пулек и коробок
    tank_object.shot(bullets, boxes)

    # Отображение спрайта танка
    tank_object.update()
    # Объекту tank1 передается список [(x, y), (x1, y1), ...] с содержанием координат коробок
    tank_object.get_boxes_coordinates([class_instance.coordinates for class_instance in field_of_boxes.boxes])

    # Нажимаемые клавиши, переменная position для сохранения позиции
    keys_get_pressed = pg.key.get_pressed()

    # Отрисовка меню, открываемое на кнопку "esc"
    menu.draw()

    # Обновление экрана
    pg.display.update()

    if menu.is_opened == False:
        """Сюда пишутся все события, которые не должны происходить, когда открывается меню."""
        # Передаётся класс tank1 для понимания направления танка и корректировки относительно его направления пуль
        bullets.update(tank_object)

        #Передвижение танка
        tank_object.move(keys_get_pressed)

    for event in pg.event.get():

        if menu.is_opened == False:
            tank_object.generate_bullet(screen, bullets, event)

        # Открытие меню на esc
        running = menu.open(event)

        if event.type == pg.QUIT:
            running = False
            pg.quit()


pg.quit()