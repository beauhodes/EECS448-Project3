#main.py

if __name__ == "__main__":
    import pygame
    import pygame.gfxdraw
    import math
    from pygame.locals import *
    import random
    from boats import Boat
    from player import Player
    pygame.init()

    disp_width = 1080
    disp_height = 720

    #globals
    disp = pygame.display.set_mode((disp_width, disp_height))
    disp.fill((192, 192, 192))
    pygame.display.set_caption('Pokemon')
    clock = pygame.time.Clock()
    #call startScreen to load start screen

def startScreen():

def initializeFightScreen(playerTurn):

def playerTurn():
    #will contain everything done in one turn, will call other functions such as attack, AI attack, checkForWin, etc.
