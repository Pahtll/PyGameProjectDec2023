"""Создание счетчика очков"""
import pygame

kill_tank_coefficient = 0
kill_box_coefficient = 0
kill_drone_coefficient = 0
hit_tank_coefficient = 0

# 1 цифра в файле - tank_topleft, 2-ая - tank_bottomright
def get_scores():
    file = open('scores/scores.txt', mode='r')
    scores = [int(count) for count in file.read().split()]
    return scores

class ScoreTopleft(pygame.sprite.Sprite):
    def __init__(self, screen, tank):
        self.screen = screen
        self.font = pygame.font.Font('fonts/minecraft.ttf', 40)
        self.font_color = (255, 255, 255)
        self.coordinates = (200, 150)
        self.tank = tank
        self.tank_texture = tank.image_left
        self.texture_coords = (290, 150)

    def update(self):
        self.start_count = get_scores()[0]
        self.count = (self.start_count + self.tank.killed_tanks * kill_tank_coefficient +
                      self.tank.killed_drones * kill_drone_coefficient + self.tank.killed_boxes * kill_box_coefficient +
                      self.tank.hit_other_tank * hit_tank_coefficient)
        self.final_count = '000'

        if self.count in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            self.final_count = f'00{self.count}'
        elif self.count in [10, 20, 30, 40, 50, 60, 70, 80, 90]:
            self.final_count = f'0{self.count // 10}0'
        elif 11 <= self.count <= 99:
            self.final_count = f'0{self.count}'
        elif self.count in [100, 200, 300, 400, 500, 600, 700, 800, 900]:
            self.final_count = f'{self.count // 100}00'
        elif self.count / 10 == self.count // 10 and len(str(self.count)) == 3:
            self.final_count = f'{self.count}'
        elif self.count > 999:
            self.count = 0
            self.final_count = '000'
        else:
            self.final_count = f'{self.count}'

        self.rendered_font = self.font.render(self.final_count, False, self.font_color)

        self.screen.blit(self.rendered_font, self.coordinates)
        self.screen.blit(self.tank_texture, self.texture_coords)

class ScoreBottomright(pygame.sprite.Sprite):
    def __init__(self, screen, tank):
        self.screen = screen
        self.font = pygame.font.Font('fonts/minecraft.ttf', 40)
        self.font_color = (255, 255, 255)
        self.coordinates = (515, 150)
        self.tank = tank
        self.tank_texture = tank.image_right
        self.texture_coords = (470, 150)

    def update(self):
        self.start_count = get_scores()[1]
        self.count = (self.start_count + self.tank.killed_tanks * kill_tank_coefficient +
                      self.tank.killed_drones * kill_drone_coefficient + self.tank.killed_boxes * kill_box_coefficient +
                      self.tank.hit_other_tank * hit_tank_coefficient)
        self.final_count = '000'

        if self.count in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            self.final_count = f'00{self.count}'
        elif self.count in [10, 20, 30, 40, 50, 60, 70, 80, 90]:
            self.final_count = f'0{self.count // 10}0'
        elif 11 <= self.count <= 99:
            self.final_count = f'0{self.count}'
        elif self.count in [100, 200, 300, 400, 500, 600, 700, 800, 900]:
            self.final_count = f'{self.count // 100}00'
        elif self.count / 10 == self.count // 10 and len(str(self.count)) == 3:
            self.final_count = f'{self.count}'
        elif self.count > 999:
            self.count = 0
            self.final_count = '000'
        else:
            self.final_count = f'{self.count}'

        self.rendered_font = self.font.render(self.final_count, False, self.font_color)

        self.screen.blit(self.rendered_font, self.coordinates)
        self.screen.blit(self.tank_texture, self.texture_coords)

def save_scores(score_topleft, score_bottomright):
    with open('scores/scores.txt', mode='w') as file:
        file.write(f"{score_topleft.count} {score_bottomright.count}")
    file.close()

def delete_scores():
    with open('scores/scores.txt', mode='w') as file:
        file.write("0 0")
    file.close()