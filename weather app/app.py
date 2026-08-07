# using tkinter to create interface, that can be linked to backend

from pathlib import Path
from tkinter import *

window = Tk()


window.title("What Weather")
window.config(background="#242424")
window.geometry("1000x1000")


icon = PhotoImage(file="images.png")
window.iconphoto(True, icon)

label = Label(window,text="What Weather", font=("Times New Roman",40,"bold"),fg="#00ff00", bg="black")
label.pack()
label.place(y=10)







window.mainloop() # place window on screen
