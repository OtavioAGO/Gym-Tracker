class Workout:
    def __init__(self, name, exercises: list = None):
        self.name = name
        self.exercises = []

        if exercises:
            for ex in exercises:
                self.add_exercise(ex)


    def add_exercise(self, exercise_data: dict):
        exercise_name = exercise_data.get('Exercicio')
        if not exercise_name:
            raise ValueError(f"Erro ao adicionar exercicio para a rotina {self.name}: Nome do exercicio é obrigatório")
        self.exercises.append(exercise_data)

    def print_workout(self):
        print(f"\n--------{self.name}--------")
        if not self.exercises:
            print("Nenhum exercicio registrado para esse treino.")
            return
        for exercise in self.exercises:
            nome = exercise.get('Exercicio')
            sets = exercise.get('Sets') or 'N/A'
            peso_bruto = exercise.get('KG')
            kg = f"{peso_bruto}KG" if peso_bruto else 'N/A'
            print(f"{nome} - {sets} - {kg}")
