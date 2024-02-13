# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 18:30:55 2024

@author: Eshaan Gurjar
"""

from tkinter import *
import random
root = Tk()
root.geometry('400x400')

def chooseColor():
    randomnum = random.randint(0,5)
    dictionary = {"color" : ["PaleGreen3", "RosyBrown2", "bisque2", "DarkSeaGreen1", "sienna1", "maroon2"]}
    color = dictionary["color"][randomnum]
    root.configure(background = color)
    
button = Button(root, text = "Click Me", command = chooseColor)
button.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()