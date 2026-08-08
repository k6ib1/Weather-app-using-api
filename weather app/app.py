# using tkinter to create interface, that can be linked to backend

from locations import capitals
from weather import fetch_weather_data
from tkinter import *
import random


# ---------------- WINDOW ----------------

window = Tk()

window.title("What Weather")
window.config(background="#242424")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window.geometry(f"{screen_width}x{screen_height}")

icon = PhotoImage(file="images.png")
window.iconphoto(True, icon)


# ---------------- TITLE ----------------

label = Label(
    window,
    text="What Weather",
    font=("Arial", 40, "bold"),
    fg="#00ff00",
    bg="black",
    relief=RAISED,
    bd=15,
    padx=20,
    pady=20
)

label.grid(
    row=0,
    column=0,
    columnspan=2,
    pady=30
)


# ---------------- WEATHER LABELS + FRAME    ----------------

rando_frame = Frame(window,
                    bg="#151515",
                    bd=7,
                    relief = "raised",
                    )


rando_frame.place(x=30, y=140, width=500, height=800)

body_frame = Frame(window,
                    bg="#151515",
                    bd=7,
                    relief = "raised",                   
                   )

body_frame.place(x=750, y= 200, width=1700, height=1000)

capital_label = Label(
    window,
    text="Capital: -",
    font=("Arial", 18),
    bg="#242424",
    fg="white"
)

capital_label.grid(
    row=2,
    column=0,
    sticky="w",
    padx=50,
    pady=10
)


latitude_label = Label(
    window,
    text="Latitude: -",
    font=("Arial", 18),
    bg="#242424",
    fg="white"
)

latitude_label.grid(
    row=3,
    column=0,
    sticky="w",
    padx=50,
    pady=10
)


longitude_label = Label(
    window,
    text="Longitude: -",
    font=("Arial", 18),
    bg="#242424",
    fg="white"
)

longitude_label.grid(
    row=4,
    column=0,
    sticky="w",
    padx=50,
    pady=10
)


elevation_label = Label(
    window,
    text="Elevation: -",
    font=("Arial", 18),
    bg="#242424",
    fg="white"
)

elevation_label.grid(
    row=5,
    column=0,
    sticky="w",
    padx=50,
    pady=10
)


hourly_label = Label(
    window,
    text="Hourly Data:",
    font=("Arial", 18),
    bg="#242424",
    fg="white"
)

hourly_label.grid(
    row=6,
    column=0,
    sticky="w",
    padx=50,
    pady=20
)



# ---------------- RANDOM BUTTON ----------------

button = Button(
    window,
    text="Random Capital!",
    bg="black",
    fg="#00ff00",
    font=("Arial", 20),
    cursor="hand1"
)


# ---------------- RANDOM FUNCTION ----------------

def click():

    rando_capital = random.choice(capitals)

    data = fetch_weather_data(rando_capital)

    capital_label.config(
        text=f"Capital: {rando_capital}"
    )

    latitude_label.config(
        text=f"Latitude: {data['latitude']} ° "
    )

    longitude_label.config(
        text=f"Longitude: {data['longitude']} °"
    )

    elevation_label.config(
        text=f"Elevation: {data['elevation']} m "
    )
    hourly_label.config(
    text=data["hourly"],
    font=("Courier New", 12),
    justify="left"
    )


button.config(command=click)

button.grid(
    row=1,
    column=0,
    padx=50,
    pady=20,
    sticky="w"
)


# ---------------- ENTRY AREA ---------------------------
title = Label(window, text="Enter a location below:",
                font=("Arial",20),
                bg="#151515",
                bd=7,
                relief = "raised",
                fg="#00ff00"
               )
title.place(x=800, y= 210,)

location_entry = Entry(font=("Arial",25), width=50)
location_entry.place(x=800, y= 260,)

def submit():

    try:
        location = location_entry.get()
        entry_data = fetch_weather_data(location)

        latitude_name.config(
            text=f"Latitude: {entry_data['latitude']} °"
        )

        longitude_name.config(
            text=f"Longitude: {entry_data['longitude']} °"
        )

        elevation_name.config(
            text=f"Elevation: {entry_data['elevation']} m"
        )
        hourly_name.config(
            text=f"\nHourly Data:\n {entry_data["hourly"]}",
            font=("Courier New", 12),
            justify="left"
        )

    except Exception:
        latitude_name.config(text="Latitude: Not found")
        longitude_name.config(text="Longitude: Not found")
        elevation_name.config(text="Elevation: Not found")
        hourly_name.config(text="Hourly Data: Not found")


longitude_name = Label(body_frame, text="Longitude: ",bg="#151515",bd=7,fg="#00ff00", font=("Arial",30))
longitude_name.place(x=45,y=200)

latitude_name = Label(body_frame, text="Latitude: ",bg="#151515",bd=7,fg="#00ff00", font=("Arial",30))
latitude_name.place(x=45,y=270)

elevation_name = Label(body_frame, text="Elevation: ",bg="#151515",bd=7,fg="#00ff00", font=("Arial",30))
elevation_name.place(x=45,y=340)

hourly_name = Label(body_frame, text="Hourly: ",bg="#151515",bd=7,fg="#00ff00", font=("Arial",30))
hourly_name.place(x=45,y=410)


submit = Button(window,text="submit",command=submit)
submit.place(x=800,y=310)










# ---------------- GRID CONFIGURATION ----------------

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)


window.mainloop()
