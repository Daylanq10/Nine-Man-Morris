"""
Upsetti Spaghetti Coders
Kole Keeney, Chris Munns, Daylan Quinn and Greg Robson
10/23/20
CS 449
Nine Men's Morris main file
"""


import pygame
import game_functions

pygame.init()

# Set title of screen
pygame.display.set_caption("Nine Men's Morris")

# Menu function allows for everything to be called as needed. This is where all the magic happens.
game_functions.menu()

# Done! Time to quit.
pygame.quit()
