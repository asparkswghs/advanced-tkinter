#!/usr/bin/env python
import tkinter

# Functions

# Window Properties
window = tkinter.Tk()
window.title("Advanced Tkinter Tutorial")
window.geometry("600x400")


# Create Labels
label_side_a = tkinter.Label(window, text = 'Side A:')
label_side_b = tkinter.Label(window, text = 'Side B:')

# Create Text Boxes
text_side_a = tkinter.Entry(window)
text_side_b = tkinter.Entry(window)

# Create Buttons
button_calculate = tkinter.Button(window, text = 'Calculate')

# Add GUI Widgets to Grid
label_side_a.grid(row = 0, column = 0, padx = 10, pady = 10)
label_side_b.grid(row = 1, column = 0, padx = 10, pady = 10)
text_side_a.grid(row = 0, column = 1, padx = 10, pady = 10)
text_side_b.grid(row = 1, column = 1, padx = 10, pady = 10)
button_calculate.grid(row = 2, column = 1, padx = 10, pady = 10)

# Present Window
window.mainloop()
