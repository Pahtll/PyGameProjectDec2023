"""Создание эскейп меню"""
from menu import Button
import run, pygame as pg, score, save_script


class EscapeMenu:
    """
    Класс EscapeMenu создаёт меню, которое открывается на клавишу escape, и имеет две кнопки: продолжить и выйти.
    \n buttonResume - кнопка продолжить
    \n buttonExit - кнопка выйти
    \n is_opened - флаг, который показывает открыто ли меню или нет.
    """
    def __init__(self, screen):
        self.screen = screen
        self.button_resume = Button(screen, 200, 400, 70, "Продолжить")
        self.button_main_menu = Button(screen, 300, 400, 70, "Выйти в главное меню")
        self.is_opened = False

    def draw(self, score_topleft, score_bottomright):
        """Рисует кнопки, если меню открыто."""

        if self.is_opened:
            self.button_resume.draw()
            self.button_main_menu.draw()
            score_topleft.update()
            score_bottomright.update()

    def open(self, event, menu, score_topleft, score_bottomright):
        """
        Открывает меню и обновляет кнопки, если клавиша escape нажата. Функция возвращает True, если кнопка
        выход не была нажата и False в противном случае. Затем это значение передаётся в переменную running.
        """

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self.is_opened = not self.is_opened

        if self.is_opened:

            self.button_resume.update(event)
            self.button_main_menu.update(event)

            if self.button_resume.state == 'pressed':
                self.button_resume.state = 'normal'
                self.is_opened = False

            if self.button_main_menu.state == 'pressed':
                self.button_main_menu.state = 'normal'
                score.save_scores(score_topleft, score_bottomright)
                menu.is_opened = True
                self.is_opened = False
                # Запускает процесс перезагрузки и сохраняет текущий стейт игры
                save = save_script.Save()
                save.drone_kill()
                run.run_game()
