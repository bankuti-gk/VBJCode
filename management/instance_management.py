import os
import string
from shutil import rmtree
from utilities import search

def add_instance(cluster_path):
    os.system("cls")
    print("Add meg a számítógép nevét!")
    name = input(">> ")

    if not name:
        return
    
    print("Add meg a millimagok számát és memóriakapacitást (MB) szóközzel elválasztva.")
    resources = [int(x) for x in input(">> ").split()]
    valid_characters = list(string.ascii_letters) + list(string.digits)

    instance_path = os.path.join(cluster_path, name)

    print(instance_path)

    if os.path.isdir(instance_path):
        print(f"Ilyen nevű számítógép már létezik! ({name})")
        input(">> ")
        return

    for c in name:
        if c not in valid_characters:
            print(f"Hiba! Helytelen karakter: {c}")
            input(">> ")
            return

    os.makedirs(f"{cluster_path}/{name}")
    with open(f"{cluster_path}/{name}/.szamitogep_config", 'x') as file:
        file.write(f"{resources[0]}\n{resources[1]}")

def delete_instance(cluster_path):
    os.system("cls")
    computer = search.get_computer(cluster_path)
    computer_path = os.path.join(cluster_path, computer)

    processes = search.get_computer_data(computer_path, "processes")
    
    if processes:
        print(f"Hiba: Létezik futó folyamat a számítógépen!\n")
        print("\n<---------------------->\n")
        for process in processes:
            with open(os.path.join(cluster_path, computer, process), encoding="utf-8") as p:
                data = p.readlines()
            print(f"Név:\t{process}\nIndítás ideje:\t{data[0].strip()}\nStátusz:\t{data[1].strip()}\n")
        print("<---------------------->\n")
    else:
        print(f"\nGép törölve: {computer}")
        rmtree(os.path.join(cluster_path, computer))
    
    input(">> ")