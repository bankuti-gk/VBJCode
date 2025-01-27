import os
import string

def monitoring(root_directory):
    neve = []
    azonosito = []
    darab = []
    os.system("cls")
    mappak = os.listdir(root_directory)

    for i in range(len(mappak)):
        print(mappak[i])
        config = open(root_directory+f"\\{mappak[i]}\\.szamitogep_config")
        config = config.readlines()
        for j in range(len(config)):
            lista = os.listdir(root_directory+f"\\{mappak[i]}")
            lista.remove(".szamitogep_config")
        print(f"\tMAX \tElérhető")
        for j in range(int(len(config)/2)):
            proci_hasznalat = 0
            ram_hasznalat = 0
            for k in range(len(lista)):
                hasznalt = open(root_directory+f"\\{mappak[i]}\\{lista[k]}")
                hasznalt = hasznalt.readlines()
                proci_hasznalat += int(hasznalt[2].strip())
                ram_hasznalat += int(hasznalt[3].strip())
            print("\t" + config[j].strip() + "\t" + str(int(config[j]) - proci_hasznalat))
            print("\t" + config[j].strip() + "\t" + str(int(config[j]) - ram_hasznalat))
        print()

    return

def add_instance(root_directory):
    name = ''.join([x for x in input("Add meg a számítógép nevét: ")])
    resources = [int(x) for x in input("Add meg a millimagok számát és memóriakapacitást (MB) szóközzel elválasztva: ").split()]
    letters = list(string.ascii_letters)
    digits = list(string.digits)

    for c in name:
        if c not in letters and c not in digits:
            exit("baj van fonok")

    os.makedirs(f"{root_directory}/{name}")
    with open(f"{root_directory}/{name}/.szamitogep_config", 'x') as file:
        file.write(f"{resources[0]}\n{resources[1]}")

def bekeres(egyezni, kiiratas):
    bemenet = int(input(kiiratas))
    while bemenet != egyezni:
        print("Rossz a bemenet")
        bemenet = int(input(kiiratas))
    return bemenet

def display_menu():
    print("1: Monitoring\n2: Add Instance")

def main():
    befele = ""
    root_directory = ""
    while True:
        cluster_name = input("Add meg a cluster mappa nevét: ")
        root_directory = os.path.join(os.getcwd(), cluster_name)
        if os.path.exists(root_directory):
            break
        else:
            print(f"Hiba! Nem található {cluster_name} nevű mappa a jelenlegi könyvtárban. ({os.getcwd()})")

    while befele.lower() != "stop":
        os.system("cls")
        display_menu()
        befele = input().lower()
        if befele == "1":
            monitoring(root_directory)
            input()
        elif befele == "2":
            add_instance(root_directory)
    os.system("cls")

if __name__ == "__main__":
    main()