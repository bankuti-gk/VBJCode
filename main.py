import os

from monitoring import monitoring
from utilities import display_menu, run_checks
from management import add_instance

def main():
    user_input = ""
    root_directory = ""
    while True:
        cluster_name = input("Add meg a cluster mappa nevét: ")
        root_directory = os.path.join(os.getcwd(), cluster_name)
        if os.path.exists(root_directory):
            break
        else:
            print(f"Hiba! Nem található {cluster_name} nevű mappa a jelenlegi könyvtárban. ({os.getcwd()})")

    while user_input.lower() != "stop":
        run_checks(root_directory)
        os.system("cls")
        display_menu()
        user_input = input()
        if user_input == "1":
            monitoring(root_directory)
            input()
        elif user_input == "2":
            add_instance(root_directory)
    os.system("cls")

if __name__ == "__main__":
    main()