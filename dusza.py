### C:\Users\User\Documents\Dusza_VBJCode\cluster0

import os
import string

def monitoring(root_directory):
    neve = []
    azonosito = []
    darab = []
    os.system("cls")
    mappak = os.listdir(root_directory)
    mappak.remove(".klaszter")

    for i in range(len(mappak)):
        print(mappak[i])
        
        config = open(root_directory+f"\\{mappak[i]}\\.szamitogep_config")
        config = config.readlines()
        for j in range(len(config)):
            lista = os.listdir(root_directory+f"\\{mappak[i]}")
            lista.remove(".szamitogep_config")
        print(f"\tMAX \tElérhető")
        for asd in range(int(len(config)/2)):
            for k in range(len(lista)):
                proci_hasznalat = 0
                ram_hasznalat = 0
                hasznalt = open(root_directory+f"\\{mappak[i]}\\{lista[k]}")
                hasznalt = hasznalt.readlines()
                proci_hasznalat += int(hasznalt[2].strip())
                ram_hasznalat += int(hasznalt[3].strip())
            print("\t" + config[asd].strip() + "\t" + str(int(config[asd]) - proci_hasznalat))
            asd += 1
            print("\t" + config[asd].strip() + "\t" + str(int(config[asd]) - ram_hasznalat))
        print()

    return

def add_instance():
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
    global root_directory 
    root_directory = input("Add meg a gyökérkönyvtár PONTOS elérési útját: ")
    while befele != "stop":
        os.system("cls")
        display_menu()
        befele = input().lower()
        if befele == "1":
            monitoring(root_directory)
            input()
        elif befele == "2":
            add_instance()
    os.system("cls")

main()