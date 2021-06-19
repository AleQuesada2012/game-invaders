from tkinter import *
import pygame
import time
import os  # path management
from threading import Thread
import threading
from PIL import Image, ImageTk
from pygame.locals import *  # import all


# image loader
def load_image(Name, Window):
    load = Image.open("images\\homePage.png")
    render = ImageTk.PhotoImage(load)
    img = Label(Window, image = render)
    img.image = render
    img.place(x=0, y=0)


# initialize tkinter
MainWindow = Tk()
MainWindow.title("Home")
MainWindow.geometry('800x600')  # basic res
MainWindow.resizable(width=NO, height=NO)

MW_canvas = Canvas(MainWindow, width=800, height=600, bg="white")
MW_canvas.place(x=0, y=0)


load = Image.open("images\\homePage.png")
render = ImageTk.PhotoImage(load)
img = Label(MW_canvas, image = render)
img.image = render
img.place(x=0, y=0)


# basic logic during a level

def play_btn():
    """
    button function to start the game
    """
    MainWindow.withdraw()

def about_btn():
    MainWindow.withdraw()
    about_window()

btn_about = Button(MW_canvas, text = "About", font = ("freesansbold", 12), command = about_btn, fg = "#F0F0F0", bg  = "grey")
btn_about.place(x = 400, y = 400)


def about_window():
    about_text = \
        """
        Costa Rica
        Instituto Tecnológico de Costa Rica
        Área de Ingeniería en Computadores
        Curso: Taller de Programación, CE-1102
        Grupo X
        Año 2021
        Proyecto III
        Profesor:
        Leonardo Araya
        Versión:
        1.0.0
        Desarrolladores/Autores:
        Michael
        Carné: XXXXX
        Andrés
        Carné: XXXXXX
        """
    instructions = \
        """
        Hints:
        Para mover al jugador se utilizan las
        flechas direccionales. Debe ingresar
        un nombre antes de comenzar el juego.
        Para ver la tabla de puntajes, debe cerrar
        esta ventana y acceder a la ventana de 
        mejores puntajes por medio del botón
        en la ventana principal.
        """

    About = Toplevel()
    About.title("About")
    About.geometry("800x600")
    About.resizable(width=NO, height=NO)

    AB_canvas = Canvas(About, width = 800, height= 600, bg = '#FCFCFC')
    AB_canvas.pack(anchor = NW, fill = Y)

    load = Image.open("images\\homePage.png")
    render = ImageTk.PhotoImage(load)
    #img = AB_canvas.create_image(0, 0, "render")

    AB_canvas.info = about_text
    AB_canvas.help = instructions
    AB_canvas.create_image(0,0, )
    AB_canvas.create_text(200,175, text = about_text, justify = CENTER, font = ("Consolas", 11))
    AB_canvas.create_text(590, 175, text = instructions, justify = CENTER, font= ("Consolas", 11))
    AB_close = Button(AB_canvas, command =lambda : close_window(About, MainWindow), text = "Regresar", bg = 'grey', fg = "#F0F0F0",
                      font = ("Consolas",12), height= 2, width = 7, bd = 1)

    AB_close.place(x = 380, y = 550, anchor = CENTER)


def close_window(widgetObj, parent = ''):
    """
    lambda-assignable function used to close any window
    :param widgetObj: the window to be closed
    :param parent: the window to open after the previous window was closes
    :return:
    """
    widgetObj.destroy()
    if parent != '':
        # function that reloads info from the txt files to be created
        parent.deiconify()


# algoritmo Quicksort
def quick_sort(players):
    # line format: name-score\n
    pass


MainWindow.protocol("WM_DELETE_WINDOW", lambda : close_window(MainWindow))
MainWindow.mainloop()