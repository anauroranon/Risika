from src.deck import Deck
from src.dice import Dice
from src.territory import Territory
from src.card import Card, Symbol
from src.paths import board_path, cards_paths, red_dice_paths, blue_dice_paths

from tkinter import *
from PIL import Image, ImageTk


def initialize_deck():
    cards_images = create_cards_images()
    mazzo = Deck([Card("Lingue", Symbol.COFFEE, cards_images[0]),
                  Card("Giurisprudenza", Symbol.COFFEE, cards_images[1]),
                  Card("Infermieristica", Symbol.COFFEE, cards_images[2]),
                  Card("Medicina", Symbol.COFFEE, cards_images[3]),
                  Card("Tossicologia", Symbol.COFFEE, cards_images[4]),
                  Card("Scienze della natura", Symbol.COFFEE, cards_images[5]),
                  Card("Ingegneria Chimica", Symbol.COFFEE, cards_images[6]),
                  Card("Ingegneria Elettronica", Symbol.COFFEE, cards_images[7]),
                  Card("Fisica", Symbol.COFFEE, cards_images[8]),
                  Card("Matematica", Symbol.COFFEE, cards_images[9]),
                  Card("Chimica", Symbol.COFFEE, cards_images[10]),
                  Card("Architettura", Symbol.COFFEE, cards_images[11]),
                  Card("Filosofia", Symbol.BEER, cards_images[12]),
                  Card("Lettere", Symbol.BEER, cards_images[13]),
                  Card("Scienze politiche", Symbol.BEER, cards_images[14]),
                  Card("Scienze motorie", Symbol.BEER, cards_images[15]),
                  Card("Biologia", Symbol.BEER, cards_images[16]),
                  Card("Ingegneria meccanica", Symbol.BEER, cards_images[17]),
                  Card("Ingegneria Civile", Symbol.BEER, cards_images[18]),
                  Card("Informatica", Symbol.BEER, cards_images[19]),
                  Card("Psicologia", Symbol.WINE, cards_images[20]),
                  Card("Pedagogia", Symbol.WINE, cards_images[21]),
                  Card("Economia", Symbol.WINE, cards_images[22]),
                  Card("Odontoiatria", Symbol.WINE, cards_images[23]),
                  Card("CTF", Symbol.WINE, cards_images[24]),
                  Card("Farmacia", Symbol.WINE, cards_images[25]),
                  Card("Jolly", Symbol.JOLLY, cards_images[26]),
                  Card("Jolly", Symbol.JOLLY, cards_images[26])])

    return mazzo


def initialize_territories():
    territories = [
        Territory("Lingue", centroid=[192, 282]),
        Territory("Giurisprudenza", centroid=[325, 321]),
        Territory("Infermieristica", centroid=[621, 394]),
        Territory("Medicina", centroid=[559, 425]),
        Territory("Tossicologia", centroid=[476, 198]),
        Territory("Scienze della natura", centroid=[639, 230]),
        Territory("Ingegneria Chimica", centroid=[680, 129]),
        Territory("Ingegneria Elettronica", centroid=[805, 222]),
        Territory("Fisica", centroid=[968, 424]),
        Territory("Matematica", centroid=[870, 513]),
        Territory("Chimica", centroid=[820, 421]),
        Territory("Architettura", centroid=[681, 355]),
        Territory("Filosofia", centroid=[258, 144]),
        Territory("Lettere", centroid=[213, 195]),
        Territory("Scienze politiche", centroid=[299, 426]),
        Territory("Scienze motorie", centroid=[662, 495]),
        Territory("Biologia", centroid=[546, 194]),
        Territory("Ingegneria Meccanica", centroid=[736, 145]),
        Territory("Ingegneria Civile", centroid=[916, 131]),
        Territory("Informatica", centroid=[951, 518]),
        Territory("Psicologia", centroid=[399, 56]),
        Territory("Pedagogia", centroid=[348, 182]),
        Territory("Economia", centroid=[269, 312]),
        Territory("Odontoiatria", centroid=[493, 390]),
        Territory("CTF", centroid=[503, 109]),
        Territory("Farmacia", centroid=[433, 268])]

    return territories


def initialize_dice(color):
    if color == "red":
        dice_images = create_dice_images(red_dice_paths)

    else:  # color == "blue"
        dice_images = create_dice_images(blue_dice_paths)

    dice = Dice(color, dice_images)

    return dice


def create_dice_images(dice_paths):
    dice_images = list(range(len(dice_paths)))

    for i in range(len(dice_paths)):
        dice_images[i] = open_image(dice_paths[i], 70, 70)

    return dice_images


def create_cards_images():
    cards_images = list(range(len(cards_paths)))

    for i in range(len(cards_paths)):
        cards_images[i] = open_image(cards_paths[i], 100, 160)

    return cards_images


def initialize_board():
    return open_image(board_path, 1100, 570)


def open_image(image_path, size_x, size_y):
    img = Image.open(image_path)
    img = img.resize((size_x, size_y), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    return img
