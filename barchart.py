import tkinter
from tkinter import *
import random
r = lambda: random.randint(0,255)
root = Tk()

root.minsize(320,400)

canvas_height = 23
canvas_width = 1024

w = Canvas(root, width=canvas_width, height=canvas_height)
w.pack()
w.create_rectangle(5, canvas_height, 100, 2, fill='#%02X%02X%02X' % (r(),r(),r()))
w.create_rectangle(100, canvas_height, canvas_width, 2, fill='#%02X%02X%02X' % (r(),r(),r()))
w.create_text(canvas_width/2, canvas_height / 2, text='Tabla 0', fill='black')


root.mainloop() 