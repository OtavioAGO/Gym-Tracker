import csv
import os
import calendar
from datetime import datetime, date
class RoutineTracker:
    def __init__(self):
        self.file = "rotina.csv"
        self.fieldnames = ['Data', 'Treino']
        self.update_csv()
 
    def mark_workout(self, data):
        updated_rows = []
        with open(self.file, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if data.get('Data') == row.get('Data'):
                    row['Treino'] = data.get("Treino")
                updated_rows.append(row)
        self.update_rows(updated_rows)
    def update_csv(self):
        if not os.path.exists(self.file):
            year = datetime.now().year
            month = datetime.now().month
            _, num_days = calendar.monthrange(year, month)
            dates_list = [f"{day:02d}/{month:02d}/{year}" for day in range(1, num_days + 1)]
            with open(self.file, "w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=self.fieldnames)
                writer.writeheader()
                for date in dates_list:
                    writer.writerow({'Data': date, 'Treino': ''})


    def update_rows(self, rows):
        with open(self.file, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    def check_routine(self):
        with open(self.file, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(f"{row.get('Data')} - {row.get('Treino') if row.get('Treino') else 'Não treinou.'}")

