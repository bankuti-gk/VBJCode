import os
import string

def add_instance(cluster_path):
    os.system("cls")
    name = input("Add meg a számítógép nevét: ")
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