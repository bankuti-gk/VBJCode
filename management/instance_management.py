import os
import string
from shutil import rmtree

def add_instance(cluster_path):
    os.system("cls")
    name = input("Add meg a számítógép nevét: ")

    if not name:
        return
    
    resources = [int(x) for x in input("Add meg a millimagok számát és memóriakapacitást (MB) szóközzel elválasztva: ").split()]
    valid_characters = list(string.ascii_letters) + list(string.digits)

    instance_path = os.path.join(cluster_path, name)

    print(instance_path)

    if os.path.isdir(instance_path):
        print(f"Ilyen nevű számítógép már létezik! ({name})")
        input()
        return

    for c in name:
        if c not in valid_characters:
            print(f"Hiba! Helytelen karakter: {c}")
            input()
            return

    os.makedirs(f"{cluster_path}/{name}")
    with open(f"{cluster_path}/{name}/.szamitogep_config", 'x') as file:
        file.write(f"{resources[0]}\n{resources[1]}")

def delete_instance(cluster_path):
    os.system("cls")
    computers = [computer for computer in os.listdir(cluster_path) if computer != ".klaszter"]
    for i, name in enumerate(computers, 1):
        print(f"{i}: {name}")
    
    try:
        computer_id = int(input("\nAdd meg a törlendő számítógép ID-jét: ")) - 1
    except ValueError:
        return
    
    if computer_id < 0 or computer_id > len(computers):
        print("Érvénytelen ID!")
        input()
        return
    
    print(f"\nVálasztott gép:\nID: {computer_id + 1}\tNév: {computers[computer_id]}")

    processes = [process for process in os.listdir(cluster_path + "\\" + computers[computer_id]) if process != ".szamitogep_config"]
    if processes:
        print(f"Hiba: Létezik futó folyamat a számítógépen!")
        for process in processes:
            with open(cluster_path + "\\" + computers[computer_id] + "\\" + process, encoding="utf-8") as p:
                data = p.readlines()
            print(f"Név:\t{process}\nIndítás ideje:\t{data[0].strip()}\nStátusz:\t{data[1].strip()}")
    else:
        print(f"\nGép törölve: {computers[computer_id]}")
        rmtree(cluster_path + "\\" + computers[computer_id])
    
    input()