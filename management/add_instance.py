import os
import string

def add_instance(root_directory):
    name = input("Add meg a számítógép nevét: ")
    resources = [int(x) for x in input("Add meg a millimagok számát és memóriakapacitást (MB) szóközzel elválasztva: ").split()]
    valid_characters = list(string.ascii_letters) + list(string.digits)

    instance_path = os.path.join(root_directory, name)

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

    os.makedirs(f"{root_directory}/{name}")
    with open(f"{root_directory}/{name}/.szamitogep_config", 'x') as file:
        file.write(f"{resources[0]}\n{resources[1]}")