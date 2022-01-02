from src.utils import *

import os.path


script_dir = os.path.dirname(os.path.abspath(__file__))


def match(app, canvas):
    # Initializing variables
    board = initialize_board()
    territories = initialize_territories()
    deck = initialize_deck()
    blue_dice = initialize_dice("blue")
    red_dice = initialize_dice("red")

    # Adding board image
    paint_board(canvas, board)

    # Adding centroids with score
    paint_centroids(canvas, territories)

    # Adding deck
    paint_deck(canvas, deck)

    # Adding dices
    paint_both_dices(canvas, red_dice, blue_dice)

    app.mainloop()


def get_coordinates(event):
    print(event.x, event.y)


def paint_board(canvas, board):
    canvas.create_image(0, 0, image=board, anchor='nw')


def paint_oval(canvas, x, y, color):
    x1, y1 = (x - 15), (y - 15)
    x2, y2 = (x + 15), (y + 15)
    canvas.create_oval(x1, y1, x2, y2, fill=color)


def paint_text(canvas, x, y, text, color):
    canvas.create_text(x, y, text=text, fill=color, font='Helvetica 15 bold')


def paint_centroids(canvas, territories):
    for i in range(len(territories)):
        paint_oval(canvas, territories[i].centroid[0], territories[i].centroid[1], "#476042")
        paint_text(canvas, territories[i].centroid[0], territories[i].centroid[1], str(territories[i].n_troops),
                   "white")


def paint_deck(canvas, deck):
    pos_y = 600
    pos_x = 20

    for i in range(len(deck.deck)):
        canvas.create_image(pos_x, pos_y, image=deck.deck[i].image, anchor="nw")
        pos_x += 120


def paint_dice(canvas, dice, number=1):
    pos_y = 20
    if dice.color == "blue":
        pos_x = 1120
    else:
        pos_x = 1220

    canvas.create_image(pos_x, pos_y, image=dice.faces[number-1], anchor="nw")


def paint_both_dices(canvas, dice1, dice2, number1=1, number2=1):
    paint_dice(canvas, dice1, number1)
    paint_dice(canvas, dice2, number2)
