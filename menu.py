"""Здесь прописано меню, которое открывается на клавишу escape"""
import sys, pygame as pg, pygame.font, score, save_script


class Button:
    """
    Кнопка представляет с собой интерактивный объект, на который можно выводить текст
    или взаимодействовать.
    \n screen - экран на котором мы рисуем кнопку.
    \n y - высота кнопки
    \n width - ширина прямоугольника
    \n height - высота прямоугольника
    \n text - текст на кнопке
    """
    def __init__(self, screen, y, width, height, text):
        self.width = width
        self.screen = screen

        # x является константой и равен центру экрана
        self.x = (800 - width) / 2
        self.y = y
        self.rect = pg.Rect(self.x, y, width, height)
        self.rect_shadow = pg.Rect(self.x + 2, y + 2, width, height)
        self.height = height
        self.text = text
        self.color = (255, 255, 255)
        self.shadow_color = (0, 0, 0)
        self.font = pygame.font.Font('fonts/minecraft.ttf', int(height / 3))

        """
        State отвечает за состояние кнопки. Всего есть 3 состояния: 
        normal - обычное, когда ничего не происходит
        hover - когда пользователь наводится на кнопку но не нажимает. 
        pressed - когда пользователь нажал на кнопку
        """
        self.state = 'normal'

    def draw(self):
        """Функция выводит кнопку на экран."""

        pg.draw.rect(self.screen, self.shadow_color, self.rect_shadow, 6)
        pg.draw.rect(self.screen, self.color, self.rect, 6)
        text = self.font.render(self.text, True, self.color)
        text_shadow = self.font.render(self.text, True, self.shadow_color)
        position = text.get_rect(center=self.rect.center)
        shadow_position = (position[0] + 2, position[1] + 2)
        self.screen.blit(text_shadow, shadow_position)
        self.screen.blit(text, position)

    def update(self, event):
        """
        Функция update проверяет, совершались ли в этот кадр какие-либо действия с кнопкой. Если совершались,
        то обновляет её состояние.
        """

        if event.type == pg.MOUSEMOTION:

            # Пользователь двинул мышкой и координаты этого движения пришлись на кнопку, то изменить её состояние на hover
            if self.rect.x <= event.pos[0] <= self.rect.topright[0] and self.rect.y <= event.pos[1] <= self.rect.bottomleft[1]:
                self.state = 'hover'

            else:
                self.state = 'normal'

        # Если пользователь навёлся на кнопку, то подсветить её белым
        if self.state == 'hover':
            self.color = (0, 0, 0)
            self.shadow_color = (255, 255, 255)

        elif self.state == 'normal':
            self.color = (255, 255, 255)
            self.shadow_color = (0, 0, 0)

        # Если пользователь навёлся на кнопку и нажал на мышку, то состояние кнопки - pressed
        if event.type == pg.MOUSEBUTTONDOWN and self.state == 'hover':
            self.state = 'pressed'

        self.font_color = self.color


class MainMenu:
    """Главное меню, из которого происходит вход в игру и выход из неё."""
    def __init__(self, screen):
        self.screen = screen
        self.background = pg.image.load('images/backgrounds/menuBG.png')
        self.button_start = Button(screen, 150, 300, 70, "Начать игру")
        self.button_exit = Button(screen, 350, 300, 70, "Выйти из игры")
        self.button_stats = Button(screen, 250, 300, 70, "Статистика")
        self.difficulty = DifficultyChangeMenu(self.screen)
        self.stats_menu = StatsMenu(self.screen)
        self.is_opened = True

    def draw(self):
        """Отрисовывает меню, состоящее из кнопок и заднего фона """
        if self.is_opened:
            self.screen.blit(self.background, (0, 0))
            self.stats_menu.draw()
            self.difficulty.draw()
            if not self.stats_menu.is_opened and not self.difficulty.is_opened:
                self.button_start.draw()
                self.button_exit.draw()
                self.button_stats.draw()

    def update(self, event):
        """Проверка нажаты ли кнопки """
        if self.difficulty.button_difficulty_1 == 'pressed' or self.difficulty.button_difficulty_2 == 'pressed' \
                or self.difficulty.button_difficulty_3 == 'pressed':
            self.is_opened = False
        self.stats_menu.update(event)
        self.difficulty.update(event)
        if not self.stats_menu.is_opened and not self.difficulty.is_opened:
            self.button_start.update(event)
            self.button_exit.update(event)
            self.button_stats.update(event)

        if self.button_start.state == 'pressed':
            self.button_start.state = 'normal'
            self.difficulty.is_opened = True

        elif self.button_exit.state == 'pressed':
            score.delete_scores()
            sys.exit()

        elif self.button_stats.state == 'pressed':
            self.stats_menu.is_opened = True
            self.button_stats.state = 'normal'

        elif self.difficulty.button_difficulty_1.state == 'pressed':
            self.difficulty.is_opened = False
            self.is_opened = False
            self.difficulty.button_difficulty_1.state = 'normal'
            self.difficulty.difficluty = 1

        elif self.difficulty.button_difficulty_2.state == 'pressed':
            self.difficulty.is_opened = False
            self.is_opened = False
            self.difficulty.button_difficulty_2.state = 'normal'
            self.difficulty.difficluty = 2

        elif self.difficulty.button_difficulty_3.state == 'pressed':
            self.difficulty.is_opened = False
            self.is_opened = False
            self.difficulty.button_difficulty_3.state = 'normal'
            self.difficulty.difficluty = 3

        elif self.difficulty.back_to_menu.state == 'pressed':
            self.difficulty.is_opened = False
            self.difficulty.back_to_menu.state = 'normal'

class DifficultyChangeMenu:
    """Главное меню, из которого происходит вход в игру и выход из неё."""

    def __init__(self, screen):
        self.screen = screen
        self.button_difficulty_1 = Button(screen, 150, 250, 70, "1 сложность")
        self.button_difficulty_2 = Button(screen, 250, 250, 70, "2 сложность")
        self.button_difficulty_3 = Button(screen, 350, 250, 70, "3 сложность")
        self.back_to_menu = Button(screen, 500, 250, 70, "Назад")
        self.is_opened = False
        self.main_menu_need_to_close = False
        self.difficulty = 0

    def draw(self):
        """Отрисовывает меню, состоящее из кнопок и заднего фона """
        if self.is_opened:
            self.button_difficulty_1.draw()
            self.button_difficulty_2.draw()
            self.button_difficulty_3.draw()
            self.back_to_menu.draw()

    def update(self, event):
        """Проверка нажаты ли кнопки"""
        if self.is_opened:
            self.button_difficulty_1.update(event)
            self.button_difficulty_2.update(event)
            self.button_difficulty_3.update(event)
            self.back_to_menu.update(event)

        if self.button_difficulty_1.state == 'pressed':
            self.is_opened = False
            self.button_difficulty_1.state = 'normal'
            self.difficulty = 1

        elif self.button_difficulty_2.state == 'pressed':
            self.is_opened = False
            self.button_difficulty_2.state = 'normal'
            self.difficulty = 2

        elif self.button_difficulty_3.state == 'pressed':
            self.is_opened = False
            self.button_difficulty_3.state = 'normal'
            self.difficulty = 3

    def get_difficulty(self):
        return self.difficulty
      
class StatsMenu():

    def __init__(self, screen):
        self.screen = screen
        self.is_opened = False
        self.stats = save_script.Save()
        self.font = pygame.font.Font('fonts/minecraft.ttf', 20 )
        self.title_font = pygame.font.Font('fonts/minecraft.ttf', 30)
        self.font_tank_topleft_color = (0, 255, 0)
        self.font_tank_bottomright_color = (255, 255, 0)
        self.font_color = (255, 255, 255)
        self.font_shadow_color = (0, 0, 0)
        self.stats_tank_topleft_title = self.title_font.render('Статистика зелёного танка:',
                                                   True, self.font_tank_topleft_color)
        self.stats_tank_topleft_title_shadow = self.title_font.render('Статистика зелёного танка:',
                                                         True, self.font_shadow_color)

        self.stats_tank_topleft_score = self.font.render(f'Общее количество очков: {self.stats.tank_topleft_stats[0]}',
                                                   True, self.font_color)
        self.stats_tank_topleft_score_shadow = self.font.render(f'Общее количество очков: {self.stats.tank_topleft_stats[0]}',
                                                   True, self.font_shadow_color)

        self.stats_tank_topleft_kills = self.font.render(f'Количество подбитых танков: {self.stats.tank_topleft_stats[1]}',
                                                         True, self.font_color)
        self.stats_tank_topleft_kills_shadow = self.font.render(
            f'Количество подбитых танков: {self.stats.tank_topleft_stats[1]}',
            True, self.font_shadow_color)

        self.stats_tank_topleft_copter_kills = self.font.render(
            f'Количество подбитых дронов: {self.stats.tank_topleft_stats[2]}',
            True, self.font_color)
        self.stats_tank_topleft_copter_kills_shadow = self.font.render(
            f'Количество подбитых дронов: {self.stats.tank_topleft_stats[2]}',
            True, self.font_shadow_color)


        self.stats_tank_bottomright_title = self.title_font.render('Статистика жёлтого танка:',
                                                               True, self.font_tank_bottomright_color)
        self.stats_tank_bottomright_title_shadow = self.title_font.render('Статистика жёлтого танка:',
                                                                      True, self.font_shadow_color)
        self.stats_tank_bottomright_score = self.font.render(f'Общее количество очков: {self.stats.tank_bottomright_stats[0]}',
                                                         True, self.font_color)
        self.stats_tank_bottomright_score_shadow = self.font.render(
            f'Общее количество очков: {self.stats.tank_bottomright_stats[0]}',
            True, self.font_shadow_color)

        self.stats_tank_bottomright_kills = self.font.render(
            f'Количество подбитых танков: {self.stats.tank_bottomright_stats[1]}',
            True, self.font_color)
        self.stats_tank_bottomright_kills_shadow = self.font.render(
            f'Количество подбитых танков: {self.stats.tank_bottomright_stats[1]}',
            True, self.font_shadow_color)

        self.stats_tank_bottomright_copter_kills = self.font.render(
            f'Количество подбитых дронов: {self.stats.tank_bottomright_stats[2]}',
            True, self.font_color)
        self.stats_tank_bottomright_copter_kills_shadow = self.font.render(
            f'Количество подбитых дронов: {self.stats.tank_bottomright_stats[2]}',
            True, self.font_shadow_color)

        self.back_to_menu = Button(screen, 500, 250, 70, "Назад")

    def draw(self):
        if self.is_opened:

            self.back_to_menu.draw()

            self.screen.blit(self.stats_tank_topleft_title_shadow, (80 + 3, 40 + 3))
            self.screen.blit(self.stats_tank_topleft_title, (80, 40))

            self.screen.blit(self.stats_tank_topleft_score_shadow, (100 + 2, 100 + 2))
            self.screen.blit(self.stats_tank_topleft_score, (100, 100))

            self.screen.blit(self.stats_tank_topleft_kills_shadow, (100 + 2, 140 + 2))
            self.screen.blit(self.stats_tank_topleft_kills, (100, 140))

            self.screen.blit(self.stats_tank_topleft_copter_kills_shadow, (100 + 2, 180 + 2))
            self.screen.blit(self.stats_tank_topleft_copter_kills, (100, 180))


            self.screen.blit(self.stats_tank_bottomright_title_shadow, (80 + 3, 240 + 3))
            self.screen.blit(self.stats_tank_bottomright_title, (80, 240))

            self.screen.blit(self.stats_tank_bottomright_score_shadow, (100 + 2, 300 + 2))
            self.screen.blit(self.stats_tank_bottomright_score, (100, 300))

            self.screen.blit(self.stats_tank_bottomright_kills_shadow, (100 + 2, 340 + 2))
            self.screen.blit(self.stats_tank_bottomright_kills, (100, 340))

            self.screen.blit(self.stats_tank_bottomright_copter_kills_shadow, (100 + 2, 380 + 2))
            self.screen.blit(self.stats_tank_bottomright_copter_kills, (100, 380))
    def update(self, event):
        if self.is_opened:
            self.back_to_menu.update(event)
            if self.back_to_menu.state == 'pressed':
                self.is_opened = False
                self.back_to_menu.state = 'normal'

class VictoryMenu:

    def __init__(self, screen):
        self.screen = screen
        self.is_openned = False
        self.font = pygame.font.Font('fonts/minecraft.ttf', 60)
        self.font_color = (255, 255, 255)
        self.font_shadow_color = (0, 0, 0)
        self.saved_info = []
        self.save = save_script.Save()

    def draw(self, tank_topleft, tank_bottomright):

        if tank_bottomright.alive == False and tank_topleft.alive == True:

            text_shadow = self.font.render("Победа Русских!", True, self.font_shadow_color)
            text = self.font.render("Победа Русских!", True, self.font_color)
            self.is_openned = True

            if self.is_openned:
                self.screen.blit(text_shadow, (90 + 4, 250 + 4))
                self.screen.blit(text, (90, 250))

            save = save_script.Save()
            save.tank_kill(tank_topleft, tank_bottomright)

        elif tank_bottomright.alive == True and tank_topleft.alive == False:

            text_shadow = self.font.render("Victory of the USA!", True, self.font_shadow_color)
            text = self.font.render("Victory of the USA!", True, self.font_color)
            self.is_openned = True

            if self.is_openned:
                self.screen.blit(text_shadow, (70 + 4, 250 + 4))
                self.screen.blit(text, (80, 250))
            self.save.tank_kill(tank_bottomright, tank_topleft)

        elif tank_bottomright.alive == False and tank_topleft.alive == False:

            text_shadow = self.font.render("Ничья", True, self.font_shadow_color)
            text = self.font.render("Ничья", True, self.font_color)
            self.is_openned = True
            if self.is_openned:
                self.screen.blit(text_shadow, (100 + 4, 250 + 4))

