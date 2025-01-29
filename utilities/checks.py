import os

def run_checks(cluster_path):
    cluster_config = os.path.join(cluster_path, ".klaszter")

    if not cluster_config:
        print("Hiba: Nincs cluster config fájl!")
        return
    
    with open(cluster_config, encoding="utf-8") as config: 
        required_processes = {}
        lines = [line.strip() for line in config]
        cluster_data = [lines[i:i+4] for i in range(0, len(lines), 4)]

        print(cluster_data) #debug
        input() #debug



    computers = [computer for computer in os.listdir(cluster_path) if computer != ".klaszter"]

    for computer in computers:
        computer_path = os.path.join(cluster_path, computer)
        cpu_usage = 0
        ram_usage = 0
        active = 0
        processes = [process for process in os.listdir(computer_path) if process != ".szamitogep_config"]

        config_path = os.path.join(computer, ".szamitogep_config")

        if not os.path.isfile(config_path):
            print(f"Hiba: A(z) {computer} számítógépben nem található config fájl!")
            return
        
        with open(config_path, encoding="utf-8") as config:
            max_cpu, max_ram = config.readline().strip(), config.readline().strip()
            for j in range(0, len(config), 2):

                        for process in processes:
                            with open(process, encoding="utf-8") as p:
                                data = p.readlines()
                                if data[1].strip() == "AKTÍV":
                                    active += 1
                                cpu_usage += data[2]
                                ram_usage += data[3]

        if cpu_usage > max_cpu and ram_usage > max_ram:
            print(f"Hiba! A(z) {computer} számítógépben túllépésre került a CPU és a RAM kapacitása.")
        elif cpu_usage > max_cpu:
            print(f"Hiba! A(z) {computer} számítógépben túllépésre került a CPU kapacitása.")
        elif cpu_usage > max_cpu:
            print(f"Hiba! A(z) {computer} számítógépben túllépésre került a RAM kapacitása.")

        #if active > 