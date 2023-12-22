import tank
import csv


class Save:
    def __init__(self):
        self.saves_info = []
        self.tank_topleft_stats = list()
        self.tank_bottomright_stats = list()

        # Считываем из файла.
        with open("saves.csv") as csvfile:
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

    def save_overwrighting(self, tank_topleft, tank_bottomright):
        with open("saves.csv", "w") as csvfile, open("saves.csv", "r") as csvfile_r:
            csvwriter = csv.writer(csvfile)
            csvfile_reader = csv.reader(csvfile_r)

            # Поля сохранений
            fields = ['score', 'tank_kills', 'drone_kills']

            # Запись нового в сэйв.
            rows = [self.tank_topleft_stats,
                    self.tank_bottomright_stats]
            csvwriter.writerow(fields)
            csvwriter.writerows(rows)


    def score_add(self, tank_scorer, other_tank, change):
        if tank_scorer.__class__ == tank.TankTopLeft:
            self.tank_topleft_stats[0] += change
            if not other_tank.alive:
                self.tank_topleft_stats[1] += 1


        # Не дописано