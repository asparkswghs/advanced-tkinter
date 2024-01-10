#!/usr/bin/env python
import tkinter
from PIL import ImageTk, Image

# Functions
def calculate_area():
    """ Calculates area of triangle from `text_side_a` and `text_side_b`. Displays answer on `label_answer` """
    try:
        side_a = float(text_side_a.get())
        side_b = float(text_side_b.get())
        area = 0.5 * side_a * side_b # Calculate area from sides
        label_answer.config(text = f'Area: {area}') # Display solution
    except ValueError:
        label_answer.config(text = 'Error: Sides must be numbers.')

# Window Properties
window = tkinter.Tk()
window.title("Advanced Tkinter Tutorial")
window.geometry("600x400")
window.configure(
    bg = '#696969'
)
window.iconbitmap('src/freebsd.ico') # Custom Titlebar Icon


# Create Labels
label_side_a = tkinter.Label(window, text = 'Side A:', bg = '#6969f9')
label_side_b = tkinter.Label(window, text = 'Side B:', bg = '#6969f9')
label_answer = tkinter.Label(window, text = 'Area: -')

# Create Text Boxes
text_side_a = tkinter.Entry(window)
text_side_b = tkinter.Entry(window)

# Create Buttons
button_calculate = tkinter.Button(
    window, 
    text = 'Calculate', 
    command = calculate_area,
    bg = '#69f969'
)

# Create Images
image = Image.open('src/tux.png')

# Add GUI Widgets to Grid
label_side_a.grid(row = 0, column = 0, padx = 10, pady = 10)
label_side_b.grid(row = 1, column = 0, padx = 10, pady = 10)
text_side_a.grid(row = 0, column = 1, padx = 10, pady = 10)
text_side_b.grid(row = 1, column = 1, padx = 10, pady = 10)
button_calculate.grid(row = 2, column = 0, padx = 10, pady = 10)
label_answer.grid(row = 2, column = 1, padx = 10, pady = 10)

# Present Window
window.mainloop()
