import random
import string
from utilities import search
import os

def clear():
    os.system("cls")

def program_leallitas(cluster_path):
    clear()
    directories = [dir for dir in os.listdir(cluster_path) if dir != ".klaszter"]
    print("Mit töröl?")
    mit_torol = input(">> ")
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
    input(">> ")


def program_modositas(cluster_path):
    clear()
    print("Milyen programot akarsz módosítani?")
    mit_modosit = input(">> ")
    clear()
    print("Add meg a módosított millimagok számát és memóriakapacitást (MB) szóközzel elválasztva.")
    mennyire_modosit = input(">> ").split()
    clear()
    millimag = mennyire_modosit[0]
    memoria = mennyire_modosit[1]
    print("Mennyi legyen a minimum futtatandó példányok száma?")
    futatando_peldanyok = input(">> ")
    clear()


    directories = [dir for dir in os.listdir(cluster_path) if dir != ".klaszter"]
    for i in range(len(directories)):
        szamitogep_hely = cluster_path + f"\\{directories[i]}"
        dirs =[dir for dir in os.listdir(szamitogep_hely) if dir != ".szamitogep_config"]
        for ii in range(len(dirs)):
            if mit_modosit in dirs[ii].split("-")[0]:
                with open(szamitogep_hely + f"\\{dirs[ii]}", "r", encoding="UTF-8") as file:
                    sorok = file.readlines()
                with open(szamitogep_hely + f"\\{dirs[ii]}", "w", encoding="UTF-8") as file:
                    sorok[2] = f"{millimag}\n"
                    sorok[3] = memoria
                    file.writelines(sorok)
    
    klaszter = cluster_path + "\\.klaszter"
    klaster = cluster_path + "\\.klaszter"
    config = open(klaster, "r+", encoding="UTF-8")
    config_sorok = config.readlines()
    config.truncate(0)
    config = open(klaster, "w", encoding="UTF-8")
    for i in range(int(len(config_sorok)/4)):
        program = []
        for ii in range(4):
            program.append(config_sorok[i*4+ii])
        if program[0].strip() == mit_modosit:
            program[1] = f"{futatando_peldanyok}\n"
            program[2] = f"{millimag}\n"
            program[3] = f"{memoria}\n"
            config.writelines(program)
        else:
            config.writelines(program)
    input("Program adatai módosítva")
