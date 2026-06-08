import csv
from pathlib import Path
from workout import Workout

FOLDER_PATH = Path("Treinos")

class WorkoutManager:
    def __init__(self):
        self.workouts = []
        self.load_workouts()


    def load_workouts(self):
        if not FOLDER_PATH.exists():
            return

        for file_path in FOLDER_PATH.glob("*.csv"):
            workout_name = file_path.stem
            exercises = []
            with open(file_path, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    exercises.append(row)

            workout = Workout(workout_name, exercises=exercises)
            self.workouts.append(workout)

    def save_workout(self, workout: Workout):
        FOLDER_PATH.mkdir(parents=True, exist_ok=True)
        workout_path = FOLDER_PATH / f"{workout.name}.csv"
        fieldnames = ['Exercicio', 'Sets', 'KG']

        with open(workout_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(workout.exercises)

    def add_workout(self, workout: Workout):
        self.workouts.append(workout)
        self.save_workout(workout)

    def list_workouts(self):
        if not self.workouts:
            print("Nenhum treino cadastrado.")
            return

        for index, workout in enumerate(self.workouts, start=1):
            print(f"{index}. {workout.name}")

    def list_exercises(self, workout_index):
        if 1 <= workout_index <= len(self.workouts):
            self.workouts[workout_index - 1].print_workout()
        else:
            print("Opção inválida.")

    def remove_workout(self, workout_index):
        if 1 <= workout_index <= len(self.workouts):
            workout_to_remove = self.workouts.pop(workout_index-1)
            workout_path = FOLDER_PATH/f"{workout_to_remove.name}.csv"
            workout_path.unlink(missing_ok=True)
            print(f"Treino {workout_to_remove.name} removido com sucesso.")
        else:
            print("Opção inválida.")