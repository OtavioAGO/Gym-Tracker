import os
from datetime import datetime
from routine_tracker import RoutineTracker
from workout_manager import WorkoutManager
from workout import Workout
tracker = RoutineTracker()
manager = WorkoutManager()

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear_terminal()
    print("1. Marcar Presenças"
          "\n2. Consultar Presenças"
          "\n3. Consultar Treinos"
          "\n4. Adicionar Treino"
          "\n5. Remover Treino"
          "\n6. Sair")
    option = input(":")
    clear_terminal()

    if option == '1':
        print("Aviso: A marcação é feita para o dia vigente.")
        today = datetime.now().strftime("%d/%m/%Y")
        if manager.workouts:
            manager.list_workouts()
            workout_option = input("Selecione um da lista ou pressione enter para outro\n:")
            if workout_option.isdigit() and 1 <= int(workout_option) <= len(manager.workouts):
                workout_name = manager.workouts[int(workout_option) - 1].name
            else:
                workout_name = input("Nome do treino:")
        else:
            workout_name = input("Nome do treino:")
        data = {"Data" : today, "Treino" : workout_name}
        tracker.mark_workout(data)
        print(f"Treino {workout_name} marcado para {today} com sucesso.")
        input("Pressione enter para retornar ao menu.")


    elif option == '2':
        tracker.check_routine()
        input("Pressione enter para retornar ao menu.")
    elif option == '3':
        if manager.workouts:
            while True:
                clear_terminal()
                manager.list_workouts()
                print("\nPressione enter para retornar ao menu.")
                exercise_option = input("Digite o numero do treino para ver os exercicios\n: ")
                if exercise_option.isdigit() and int(exercise_option) != 0:
                    clear_terminal()
                    manager.list_exercises(int(exercise_option))
                    input("Pressione enter para retornar a lista de treinos.")
                else:
                    break
        else:
            print("Nenhum treino cadastrado.")
            input("Pressione enter para retornar ao menu.")
    elif option == '4':
        new_workout = Workout(input("Nome do treino:"))
        while True:
            print("1. Adicionar Exercicios")
            exercise_input = input("Pressione enter para retornar ao menu...\n:")
            clear_terminal()
            if exercise_input == '1':
                exercise_name = input("Nome do exercicio: ")
                sets = input("Sets:")
                kg = input("Peso atual:")
                exercise_data = {"Exercicio" : exercise_name, "Sets" : sets, "KG" : kg}
                new_workout.add_exercise(exercise_data)
            else:
                if new_workout.exercises:
                    manager.add_workout(new_workout)
                    print(f"Treino {new_workout.name} salvo e registrado com sucesso")
                    input("Pressione enter para retornar ao menu.")
                break
    elif option == '5':
        if manager.workouts:
            clear_terminal()
            manager.list_workouts()
            remove_option = input("Selecione um treino da lista para remover ou pressione enter para cancelar \n:")
            if remove_option.isdigit() and 1 <= int(remove_option) <= len(manager.workouts):
                manager.remove_workout(int(remove_option))
                print("Treino removido com sucesso")
                input("Pressione Enter para retornar ao menu.")
        else:
            clear_terminal()
            print("Nenhum registro de treino encontrado.")
            input("Pressione enter para retornar ao menu.")
    elif option == '6':
        break
    else:
        print("Opção invalida")
