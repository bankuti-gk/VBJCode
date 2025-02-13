from tkinter import *

def start_program(root):
    root.destroy()

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
    root.geometry("500x500")

    start_button = Button(root, text="Program indítása", activebackground="gray", command=lambda: start_program(root))
    start_button.pack(pady=10)

    credits_button = Button(root, text="Csapattagok", activebackground="gray", command=lambda: credits(root))
    credits_button.pack(pady=10)

    exit_button = Button(root, text="Kilépés", activebackground="gray", command=exit_program)
    exit_button.pack(pady=10)

    root.protocol("WM_DELETE_WINDOW", exit_program)

    root.mainloop()