"""Здесь прописано меню, которое открываетcя на клавишу escape"""
import pygame as pg
import pygame.font

class Button:
    """
    Кнопка представляет с собой интерактивный объект, на который можно выводить текст
    и с которым можно взаимодействовать.
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
        self.height = height
        self.text = text
        self.color = (0, 0, 0)
        self.font = pygame.font.Font(None, int(height / 1.5))
        self.font_color = self.color

        """
        State отвечает за состояние кнопки. всего есть 3 состояния: normal - обычное, когда ничего не происходит
        hover - когда пользователь наводится на кнопку но не нажимает. pressed - когда пользователь нажал на кнопку
        """
        self.state = 'normal'

    def draw(self):
        """
        Функция выводит кнопку на экран
        """
        pg.draw.rect(self.screen, self.color, self.rect, 10)
        text = self.font.render(self.text, True, self.font_color)
        position = text.get_rect(center=self.rect.center)
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
            self.color = (255, 255, 255)

        elif self.state == 'normal':
            self.color = (0, 0, 0)

        # Если пользователь навёлся на кнопку и нажал на мышку, то состояние кнопки - pressed
        if event.type == pg.MOUSEBUTTONDOWN and self.state == 'hover':
            self.state = 'pressed'

        self.font_color = self.color



class EscapeMenu:
    """
    Класс EscapeMenu создаёт меню, которое открывается на клавишу escape, и имеет две кнопки: продолжить и выйти.
    \n buttonResume - кнопка продолжить
    \n buttonExit - кнопка выйти
    \n is_opened - флаг, который показывает открыто ли меню или нет.
    """
    def __init__(self, screen):
        self.screen = screen
        self.button_resume = Button(screen, 200, 250, 70, "Продолжить")
        self.button_exit = Button(screen, 300, 250, 70, "Выход")
        self.is_opened = False

    def draw(self):
        """
        Рисует кнопки, если меню открыто
        """
        if self.is_opened:
            self.button_resume.draw()
            self.button_exit.draw()

    def open(self, event):
        """
        Открывает меню и обновляет кнопки, если клавиша escape нажата. Функция возвращает True, если кнопка
        выход не была нажата и False в противном случае. Затем это значение передаётся в переменную running.
        """
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self.is_opened = not self.is_opened


        if self.is_opened:
            self.button_resume.update(event)
            self.button_exit.update(event)
            if self.button_exit.state == 'pressed':
                return False

            if self.button_resume.state == 'pressed':
                self.button_resume.state = 'normal'
                self.is_opened = False

        return True


