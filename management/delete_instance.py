import os
from shutil import rmtree

def delete_instance(cluster_path):
    os.system("cls")
    computers = [computer for computer in os.listdir(cluster_path) if computer != ".klaszter"]
    print("Add meg a törlendő számítógép számát: ")
    for i, name in enumerate(computers, 1):
        print(f"{i}: {name}")
    
    chosen_computer = int(input())