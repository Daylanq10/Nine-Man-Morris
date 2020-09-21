from tkinter import *
import pygame

root = Tk()

C = Canvas(root, width = 800, height = 800)

def menu():
    setting = 'def'
    home = Label(root, text = "Welcome to Nine Man's Morris!")
    home.pack()

    hvh = Button(root, text = "Human v Human", command = h2h)
    hvh.pack()

    cpu = Button(root, text = "Human v CPU")
    cpu.pack()

def h2h():
    name_one = Entry(root, text = "Enter Player 1 name")
    name_one.pack()
    name_two = Entry(root, text = "Enter Player 2 name")
    name_two.pack()
    welcome = Label(root, text = "Welcome " + name_one.get() + " and " + name_two.get() + "!")
    
    
def gameboard():
    background = C.create_rectangle(100,100,700,700, fill = "grey")

    cord = 97,97,103,103
    #four corners
    a7 = C.create_oval(cord, fill = "black") 
    a1 = C.create_oval(97,697,103,703, fill = "black") 
    g7 = C.create_oval(697,97,703,103, fill = "black")
    g1 = C.create_oval(697,697,703,703, fill = "black")

    #outer square
    d1 = C.create_oval(397,697,403,703, fill = "black")
    d7 = C.create_oval(397,97,403,103, fill = "black")
    a4 = C.create_oval(97, 397, 103, 403, fill = "black")
    g4 = C.create_oval(697, 397, 703, 403, fill = "black")

    #middle square

    b2 = C.create_oval(197, 597, 203, 603, fill = "black")
    d2 = C.create_oval(397, 597, 403, 603, fill = "black")
    f2 = C.create_oval(597, 597, 603, 603, fill = "black")
    b4 = C.create_oval(197, 397, 203, 403, fill = "black")
    f4 = C.create_oval(597, 397, 603, 403, fill = "black")
    b6 = C.create_oval(197, 197, 203, 203, fill = "black")
    d6 = C.create_oval(398, 197, 403, 203, fill = "black")
    f6 = C.create_oval(597, 197, 603, 203, fill = "black")

    #inner square

    c3 = C.create_oval(297, 497, 303, 503, fill = "black")
    d3 = C.create_oval(397, 497, 403, 503, fill = "black")
    e3 =  C.create_oval(497, 497, 503, 503, fill = "black")
    c4 = C.create_oval(297, 397, 303, 403, fill = "black")
    e4 = C.create_oval(497, 397, 503, 403, fill = "black")
    c5 = C.create_oval(297, 297,303, 303, fill = "black")
    d5 = C.create_oval(397, 297, 403, 303, fill = "black")
    e5 = C.create_oval(497, 297, 503, 303, fill = "black")

    #cross lines
    left_cross = C.create_line(100, 400, 300, 400, width = 2) #a4-c4
    right_cross = C.create_line(500, 400, 700, 400, width = 2) #e4-g4
    top_cross = C.create_line(401, 100, 401, 300, width = 2) #d5-d7
    bottom_cross = C.create_line(401, 500, 401, 700, width = 2) #d1-d3

    #middle box lines
    left_mb = C.create_line(201, 200, 201, 600, width = 2) #b2-b6
    right_mb = C.create_line(601, 200, 601, 600, width = 2) #f2-f6
    top_mb = C.create_line(200, 200, 600, 200, width = 2) #b6-f6
    bottom_mb = C.create_line(200, 600, 600, 600, width = 2) #b2-f2

    #inner box lines
    left_ib = C.create_line(301, 300, 301, 500, width = 2) #c3-c5
    right_ib = C.create_line(501, 300, 501, 500, width = 2) #e3-e5
    top_ib = C.create_line(300, 300, 500, 300, width = 2) #c5-e5
    bottom_ib = C.create_line(300, 500, 500, 500, width = 2)#c3-e3


gameboard()
#also a menu function that has clickable buttons, however doesn't go from menu to game itself


C.pack()
root.mainloop()

