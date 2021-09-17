import tkinter
from tkinter import *
import random
r = lambda: random.randint(0,255)
root = Tk()

root.minsize(320,240)

canvas_height = 23
canvas_width = 315

w = Canvas(root, width=canvas_width, height=canvas_height)
w.pack()
w.create_rectangle(5, canvas_height, canvas_width, 2, fill='#%02X%02X%02X' % (r(),r(),r()))
w.create_rectangle(5, canvas_height, 100, 2, fill='#%02X%02X%02X' % (r(),r(),r()))
w.create_text(canvas_width/2, canvas_height / 2, text='Tabla 0', fill='white')

a = 1.0 # More complicated code creates this float between 0.00 and 1.00. It is a percentage of the desired 'blue rectangle' width
b = int(a * canvas_width)

root.mainloop() 