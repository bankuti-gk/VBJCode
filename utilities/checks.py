import os
from utilities import search

def run_checks(cluster_path):
    cluster_config = os.path.join(cluster_path, ".klaszter")
    running_processes = {}

    if not os.path.isfile(cluster_config):
        print("Hiba: Nincs cluster config fájl!")
        return
    
    required_processes = search.get_cluster_data(cluster_config)

    computers = [computer for computer in os.listdir(cluster_path) if computer != ".klaszter"]

    for computer in computers:
        computer_path = os.path.join(cluster_path, computer)
        cpu_usage = 0
        ram_usage = 0
        active = 0
        processes = [process for process in os.listdir(computer_path) if process != ".szamitogep_config"]

        config_path = os.path.join(cluster_path, computer, ".szamitogep_config")

        if not os.path.isfile(config_path):
            print(f"Hiba: A(z) {computer} számítógépben nem található config fájl!")
            input(">> ")
            return
        
        with open(config_path, encoding="utf-8") as config:
            max_cpu, max_ram = int(config.readline().strip()), int(config.readline().strip())

            for process in processes:
                with open(os.path.join(cluster_path, computer, process), encoding="utf-8") as p:
                    data = p.readlines()
                    if data[1].strip() == "AKTÍV":
                        active += 1
                    cpu_usage += int(data[2])
                    ram_usage += int(data[3])

        if cpu_usage > max_cpu and ram_usage > max_ram:
            print(f"Hiba! A(z) {computer} számítógépben túllépésre került a CPU és a RAM kapacitása.")
            input()
            return
        elif cpu_usage > max_cpu:
            print(f"Hiba! A(z) {computer} számítógépben túllépésre került a CPU kapacitása.")
            input()
            return
        elif cpu_usage > max_cpu:
            print(f"Hiba! A(z) {computer} számítógépben túllépésre került a RAM kapacitása.")
            input()
            return

