import os

from monitoring import monitoring
from utilities import display_menu, run_checks
from management import add_instance, delete_instance

possible_inputs = {
    1 : monitoring,
    2 : add_instance,
    3 : delete_instance
}


def main():
    while True:
        cluster_path = input("Add meg a cluster mappa pontos elérési útvonalát: ")
        if os.path.exists(cluster_path):
            break
        else:
            print(f"Hiba! Nem található mappa a megadott útvonalon: {cluster_path}")

    while True:
        os.system("cls")
        run_checks(cluster_path)
        display_menu()
        user_input = int(input())
        if user_input in possible_inputs:
            possible_inputs[user_input](cluster_path)
        elif user_input == 0:
            break
        else:
            print("Érvénytelen választás!")
            input()

if __name__ == "__main__":
    main()

#asd