# using tkinter to create interface, that can be linked to backend

from pathlib import Path
from tkinter import *

window = Tk()


window.title("What Weather")
window.config(background="#242424")
window.geometry("1000x1000")


icon = PhotoImage(file="images.png")
window.iconphoto(True, icon)

label = Label(window,
            text="What Weather",
            font=("Arial",40,"bold"),
            fg="#00ff00", 
            bg="black",
            relief=RAISED,
            bd=15,
            padx=20,
            pady=20)
label.pack()








window.mainloop() # place window on screen
