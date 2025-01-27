import os
import string

def monitoring(root_directory):
    os.system("cls")
    directories = [dir for dir in os.listdir(root_directory) if dir != ".klaszter"]
    
    for dir in directories:
        print(dir)
        config_path = os.path.join(root_directory, dir, ".szamitogep_config")

        if not os.path.isfile(config_path):
            print(f"Hiba! Nincs konfigurációs fájl itt: {config_path}")
            exit()

        with open(config_path) as config_file:
            config = [int(line.strip()) for line in config_file]

        files = [file for file in os.listdir(os.path.join(root_directory, dir)) if file != ".szamitogep_config"]

        print(f"\tMAX \tElérhető")

        for j in range(0, len(config), 2):
            max_cpu, max_ram = config[j], config[j + 1]
            cpu_usage = 0
            ram_usage = 0

            for file in files:
                file_path = os.path.join(root_directory, dir, file)
                with open(file_path) as file:
                    data = file.readlines()
                    cpu_usage += int(data[2].strip())
                    ram_usage += int(data[3].strip())
            print(f"\t{max_cpu}\t{cpu_usage}")
            print(f"\t{max_ram}\t{ram_usage}")
        print()

    return

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

def display_menu():
    print("1: Monitoring\n2: Add Instance")

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