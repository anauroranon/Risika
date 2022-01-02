from src.match import match

from tkinter import *


def game():
    app = Tk()
    app.geometry("1600x900")

    canvas = Canvas(app, bg="white")
    canvas.pack(anchor='nw', fill='both', expand=1)

    match(app, canvas)

    app.mainloop()
