from tkinter import *
from tkinter import font as tkFont
import os

def start_program(root):
    root.destroy()

def open_readme():
    os.startfile("readme.txt")

def open_documentation():
    os.startfile("VBJCode Dokumentáció.pdf")


def credits(root):
    window = Toplevel(root)
    window.title("Cluster Command Center | Credits")
    window.geometry("500x150")
    Label(window, text="Bánka Levente - Dokumentáció, Trello\nBerecz Balázs - Programozás, dokumentáció\nJuhász Nándor - Csapatkapitány, programozás", font=("Times New Roman", 15)).pack()

def exit_program():
    quit()


def create_window():
    root = Tk()
    root.title("Cluster Command Center | Main")
    root.geometry("1920x1080")

    szia = tkFont.Font(family='Helvetica', size=36, weight='bold')

    image = PhotoImage(file="hatter3.png")
    background_label = Label(root, image=image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    start_button = Button(root, text="Program indítása", activebackground="gray", command=lambda: start_program(root), height=1, width=15, font=szia)
    start_button.pack(pady=10)

    credits_button = Button(root, text="Csapattagok", activebackground="gray", command=lambda: credits(root), height=1, width=15, font=szia)
    credits_button.pack(pady=10)

    readme_button = Button(root, text="README", activebackground="gray", command=open_readme, height=1, width=15, font=szia)
    readme_button.pack(pady=10)

    documentation_button = Button(root, text="Dokumentáció", activebackground="gray", command=open_documentation, height=1, width=15, font=szia)
    documentation_button.pack(pady=10)

    exit_button = Button(root, text="Kilépés", activebackground="gray", command=exit_program, height=1, width=15, font=szia)
    exit_button.pack(pady=225)

    root.protocol("WM_DELETE_WINDOW", exit_program)

    root.mainloop()