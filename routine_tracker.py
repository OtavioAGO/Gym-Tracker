import csv
import calendar
from pathlib import Path
from datetime import datetime, date

BASE_DIR = Path(__file__).resolve().parent

ARCHIVE_PATH = BASE_DIR / "Registro"
class RoutineTracker:
    def __init__(self):
        self.file = BASE_DIR / "rotina.csv"
        self.fieldnames = ['Data', 'Treino']
        self.archive_if_needed()
        self.update_csv()
 
    def mark_workout(self, data):
        self.archive_if_needed()
        self.update_csv()
        updated_rows = []
        with open(self.file, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if data.get('Data') == row.get('Data'):
                    row['Treino'] = data.get("Treino")
                updated_rows.append(row)
        self.update_rows(updated_rows)

    def update_csv(self):
        if not self.file.is_file():
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
        self.archive_if_needed()
        self.update_csv()
        with open(self.file, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(f"{row.get('Data')} - {row.get('Treino') if row.get('Treino') else 'Não treinou.'}")

    def archive_if_needed(self):
        if not self.file.is_file():
            return
        ano_atual = datetime.now().year
        mes_atual = datetime.now().month
        archive_needed = False
        mes_csv = None
        ano_csv = None
        
        with open(self.file, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None)
            primeira_linha = next(reader, None)

            if primeira_linha:
                data_csv = primeira_linha[0]
                partes = data_csv.split('/')
                if len(partes) == 3:
                    mes_csv = int(partes[1])
                    ano_csv = int(partes[2])

                    if mes_atual != mes_csv or ano_atual != ano_csv:
                        archive_needed = True
        if archive_needed:
            ARCHIVE_PATH.mkdir(parents=True, exist_ok=True)
            novo_nome = ARCHIVE_PATH / f"rotina_{mes_csv:02d}_{ano_csv}.csv"
            self.file.rename(novo_nome)