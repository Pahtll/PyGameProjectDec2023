import tank
import csv


class Save:
    tank_topleft_kills = 0
    tank_topleft_drones = 0
    tank_bottomright_kills = 0
    tank_bottomright_drones = 0
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
            with open("scores/scores.txt", "r") as scorefile:
                both_res_str = scorefile.readline()
                both_res_int = list(map(int, both_res_str.split(' ')))

                self.tank_topleft_stats[0] += both_res_int[0]
                self.tank_bottomright_stats[0] += both_res_int[1]
                self.tank_topleft_stats[1] += self.tank_topleft_kills
                self.tank_bottomright_stats[1] += self.tank_bottomright_kills
                self.tank_topleft_stats[2] += self.tank_topleft_drones
                self.tank_bottomright_stats[2] += self.tank_bottomright_drones


            # Поля сохранений
            fields = ['score', 'tank_kills', 'drone_kills']

            # Запись нового в сэйв.
            rows = [self.tank_topleft_stats,
                    self.tank_bottomright_stats]
            csvwriter.writerow(fields)
            csvwriter.writerows(rows)
