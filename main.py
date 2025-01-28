import os

from monitoring import monitoring
from utilities import display_menu, run_checks
from management import add_instance

def main():
    user_input = ""
    while True:
        cluster_path = input("Add meg a cluster mappa pontos elérési útvonalát: ")
        if os.path.exists(cluster_path):
            break
        else:
            print(f"Hiba! Nem található mappa a megadott útvonalon: {cluster_path}")

    while user_input.lower() != "stop":
        run_checks(cluster_path)
        os.system("cls")
        display_menu()
        user_input = input()
        if user_input == "1":
            monitoring(cluster_path)
            input()
        elif user_input == "2":
            add_instance(cluster_path)
    os.system("cls")

if __name__ == "__main__":
    main()