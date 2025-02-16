import random
import string
from utilities import search
import os
import datetime

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

def uj_peldany(cluster_path):
    ido = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    clear()
    print("Melyik számítógépen akarod futtatni az új peogrampáldányt?")
    directories = [dir for dir in os.listdir(cluster_path) if dir != ".klaszter"]
    for i in range(len(directories)):
        print(f"\t{i+1}: {directories[i]}")
    gepID = int(input(">> "))-1


    clear()
    print("Melyik programból akarsz egy új példányt futtatni?")
    klaszter = open(cluster_path+f"\\.klaszter", "r", encoding="UTF-8")
    sorok = klaszter.readlines()
    programok = []
    program_millimag = []
    program_memoriahasznalat = []
    for i in range(int(len(sorok)/4)):
        program = []
        for ii in range(4):
            program.append(sorok[i*4+ii])
        programok.append(program[0])
        program_millimag.append(program[2])
        program_memoriahasznalat.append(program[3])
        print(f"\t{i+1}: {program[0].strip()}")
    programID = int(input(">> "))-1

    gep_hely = cluster_path +f"\\{directories[gepID]}"
    dirs =[dir for dir in os.listdir(gep_hely) if dir != ".szamitogep_config"]
    millimag_hasznalt = 0
    memoria_hasznalt = 0
    for i in range(len(dirs)):
        with open(gep_hely + f"\\{dirs[i]}", "r", encoding="UTF-8") as file:
            file_sor = file.readlines()
            millimag_hasznalt += int(file_sor[2])
            memoria_hasznalt += int(file_sor[3])

    vege_volt = []
    for i in range(len(dirs)):
        if programok[programID].strip() == dirs[i].split("-")[0]:
            vege_volt.append(dirs[i].split("-")[1])
    print(vege_volt)
    input()

    betuk = ["q","w","e","r","t","z","u","i","o","p","a","s","d","f","g","h","j","k","l","y","x","c","v","b","n","m"]
    vege = ""
    for i in range(6):
        vege += betuk[random.randint(0, 25)]
    while vege in vege_volt:
        vege = ""
        for i in range(6):
            vege += betuk[random.randint(0, 25)]
    with open(cluster_path+f"\\{directories[gepID]}\\{programok[programID].strip()}-{vege}", "w", encoding="UTF-8") as irni:
        irni.write(f"{ido}\nAKTÍV\n{program_millimag[programID]}{program_memoriahasznalat[programID].strip()}")
    

    clear()
    input("Új programéldány futtatva.")

def peldany_leallitas(cluster_path):
    clear()
    print("Melyik számítógépen akarod leállítani a programpéldányt?")
    directories = [dir for dir in os.listdir(cluster_path) if dir != ".klaszter"]
    for i in range(len(directories)):
        print(f"\t{i+1}: {directories[i]}")
    gepID = int(input(">> "))-1

    gep_hely = cluster_path + f"\\{directories[gepID]}"

    dirs =[dir for dir in os.listdir(gep_hely) if dir != ".szamitogep_config"]
    for i in range(len(dirs)):
        print(f"\t{i+1}: {dirs[i]}")
    programId = int(input(">> "))-1

    os.remove(gep_hely + f"\\{dirs[programId]}")
    input("Program leállítva")