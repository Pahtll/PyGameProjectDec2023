import tank
import csv


class Save:
    tank_topleft_kills = 0
    tank_bottomright_kills = 0
    def __init__(self):
        self.saves_info = []
        self.tank_topleft_stats = list()
        self.tank_bottomright_stats = list()
        self.some_tank_killed = False

        # Считываем из файла.
        with open("saves.csv", "r", newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            fields = next(csvreader)
            for row in csvreader:
                self.saves_info.append(row)

        self.tank_topleft_stats.append(int(self.saves_info[0][0]))     # score
        self.tank_bottomright_stats.append(int(self.saves_info[1][0])) # score
        self.tank_bottomright_stats.append(int(self.saves_info[0][1])) # kills
        self.tank_topleft_stats.append(int(self.saves_info[1][1]))     # kills
        self.tank_topleft_stats.append(int(self.saves_info[0][2]))     # drone kills
        self.tank_bottomright_stats.append(int(self.saves_info[1][2])) # drone kills

    def save_overwrighting(self):
        with open("saves.csv", "w", newline='') as csvfile:
            csvwriter = csv.writer(csvfile)

            # Поля сохранений
            fields = ['score', 'tank_kills', 'drone_kills']

            # Запись нового в сэйв.
            rows = [self.tank_topleft_stats,
                    self.tank_bottomright_stats]
            csvwriter.writerow(fields)
            csvwriter.writerows(rows)
            self.some_tank_killed = False

    def drone_kill(self):
        self.tank_topleft_stats[2] += tank.TankTopLeft.killed_drones
        self.tank_bottomright_stats[2] += tank.TankBottomRight.killed_drones
        self.save_overwrighting()


    def tank_kill(self, tank_scorer, other_tank):

        if tank_scorer.__class__ == tank.TankTopLeft and not self.some_tank_killed:
            if not other_tank.alive:
                self.tank_topleft_stats[0] += 10
                self.tank_topleft_kills += 1
                self.tank_topleft_stats[1] += 1
                self.save_overwrighting()

        if tank_scorer.__class__ == tank.TankBottomRight and not self.some_tank_killed:
            if not other_tank.alive:
                self.tank_bottomright_stats[0] += 10
                self.tank_bottomright_kills += 1
                self.tank_bottomright_stats[1] += 1
                self.save_overwrighting()
