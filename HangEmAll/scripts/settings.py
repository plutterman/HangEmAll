"""
Payton Lutterman and Karma Chandia
HangEmAll
Last Updated 10-6

"""

from tkinter import *
from tkinter import ttk
from tkinter import font
import random
import pygame as pg
pg.mixer.init()
from PIL import ImageTk, Image
import os
from tkinter import messagebox

HEIGHT = 830
WIDTH = 1000
geoString = str(WIDTH)+"x"+str(HEIGHT)
TITLE = "HangEmAll"
icon_path = "assets/img/icons/hangman-game.ico"