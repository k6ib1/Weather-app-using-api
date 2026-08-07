# using tkinter to create interface, that can be linked to backend

from tkinter import *

# Configs
window = Tk()
window.title("What Weather")
window.geometry("420x420")
window.config(background="")

window.mainloop() # place window on screen


icon = PhotoImage(file='images.png')
window.iconphoto(True,icon)
