# using tkinter to create interface, that can be linked to backend

from locations import capitals
from weather import fetch_weather_data
from pathlib import Path
from tkinter import *
import random

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

def click():
    rando_capital = random.choice(capitals)
    print(f"The capital is ... {rando_capital}!")
    weather = fetch_weather_data(rando_capital)
    return(weather)



button= Button(window,
               text="Random Capital!",
               bg="black",
               fg="#00ff00"
                )
button.pack()
button.place(relx=0.15, rely=0.20, anchor=CENTER)
button.config(command=click)







window.mainloop() # place window on screen
