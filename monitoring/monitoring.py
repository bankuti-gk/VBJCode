import os

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