import os

def get_computer(cluster_path):
    computers = [computer for computer in os.listdir(cluster_path) if computer != ".klaszter"]
    for i, name in enumerate(computers, 1):
        print(f"{i}: {name}")
    
    try:
        computer_id = int(input("\nAdd meg a számítógép ID-jét:\n>> ")) - 1
    except ValueError:
        return
    
    if computer_id < 0 or computer_id > len(computers):
        print("Érvénytelen ID!")
        input(">> ")
        return
    
    print(f"\nVálasztott gép:\nID: {computer_id + 1}\tNév: {computers[computer_id]}")

    return computers[computer_id]

def get_cluster_data(cluster_config):
    with open(cluster_config, encoding="utf-8") as config: 
        lines = [line.strip() for line in config]
        cluster_data = [lines[i:i+4] for i in range(0, len(lines), 4)]
        data = {}

        for i in range(len(cluster_data)):
            data[cluster_data[i][0]] = cluster_data[i][1]
    
    return data

def get_computer_data(computer_path, requested_data):

    if requested_data == "processes":
        processes = [process for process in os.listdir(computer_path) if process != ".szamitogep_config"]
        return processes
        