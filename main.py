from tkinter import *
import pygame
import os # path management
from pygame.locals import * #import all

def main():
    #initialize pygame
    pygame.init()
    size = (800,600)
    #open the window
    screen = pygame.display.set_mode(size)
    # set the window title
    pygame.display.set_caption("Home")

    closed = False
    clock = pygame.time.Clock()
    #set the bg image
    bg_image = pygame.image.load("images\\homePage.jpg").convert() #turn image into a surface

    while (closed == False):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                closed = True
        screen.blit(bg_image, [0, 0])
        pygame.display.flip()
        clock.tick(20)
    """
    
    #initialize tkinter
    MainWindow = Tk()
    MainWindow.title("Home")
    MainWindow.geometry('800x600') #basic res
    MainWindow.resizable(width=NO,height=NO)

    MWcanvas = Canvas(MainWindow,width=800,height=600,bg="white")
    MWcanvas.place(x=0,y=0)
    """


# algoritmo Quicksort
def quick_sort(players):
    #line format: name-score\n
    pass

main()