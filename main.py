import os
import threading

from monitoring import monitoring
from utilities import display_menu, run_checks, create_window
from management import add_instance, delete_instance, program_leallitas, program_modositas, uj_peldany, peldany_leallitas

possible_inputs = {
    1 : monitoring,
    2 : add_instance,
    3 : delete_instance,
    4 : program_leallitas,
    5 : program_modositas,
    6 : uj_peldany,
    7 : peldany_leallitas
}


def main():
    x = threading.Thread(target=create_window)
    x.start()
    
    os.system("title Cluster Command Center")
    while True:
        os.system("cls")
        print("Add meg a cluster pontos útvonalát!")
        cluster_path = user_input = input(">> ").strip()
        if os.path.exists(cluster_path):
            break
        else:
            print(f"Hiba! Nem található mappa a megadott útvonalon: {cluster_path}")
            input()

    while True:
        os.system("cls")
        run_checks(cluster_path)
        display_menu()

        user_input = input(">> ").strip()
        
        # <-------------------------------------------------->
        # ez a rész érvényesíti az inputot

        if not user_input:
            print("HIBA: Nem lehet üres az input.")
            input("Nyomj meg egy gombot a folytatáshoz..")
            continue

        if not user_input.isdigit():
            print("\nHIBA: Kérlek, egy számot adj meg.")
            input("Nyomj meg egy gombot a folytatáshoz..")
            continue

        # <-------------------------------------------------->

        user_input = int(user_input)    # átalakítja az inputot integerré, hogy tudjon vele dolgozni

        if user_input == 0:
            break

        if user_input in possible_inputs:
            possible_inputs[user_input](cluster_path)
            os.system("cls")
        
        else:
                print("\nHIBA: Érvénytelen választás! (ha ezt a hibat kapod valami nagyon nem jo)")
                input("Nyomj egy gombot a folytatáshoz...")
                continue
        

if __name__ == "__main__":
    main()