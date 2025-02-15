import random
import string
from utilities import search
import os

def program_leallitas(cluster_path):
    directories = [dir for dir in os.listdir(cluster_path) if dir != ".klaszter"]
    mit_torol = input("Mit töröl?")
    for i in range(len(directories)):
        szamitogep_hely = cluster_path +f"\\{directories[i]}"
        dirs =[dir for dir in os.listdir(szamitogep_hely) if dir != ".szamitogep_config"]
        for ii in range(len(dirs)):
            if (dirs[ii].split("-"))[0] == mit_torol:
                os.remove(f"{szamitogep_hely}\\{dirs[ii]}")

    klaster = cluster_path + "\\.klaszter"
    config = open(klaster, "r+", encoding="UTF-8")
    config_sorok = config.readlines()
    config.truncate(0)
    config = open(klaster, "w", encoding="UTF-8")
    for i in range(int(len(config_sorok)/4)):
        program = []
        for ii in range(4):
            program.append(config_sorok[i*4+ii])
        if program[0].strip() != mit_torol:
            for ii in range(4):
                config.write(program[ii])
    print(f"{mit_torol} törölve")
    input()
    