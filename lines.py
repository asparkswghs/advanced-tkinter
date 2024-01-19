#!/usr/bin/env python
import tkinter

# Window Properties
window = tkinter.Tk()
window.geometry("500x400")
window.minsize(300, 300)
window.title("Drawing Lines :p")

# Triangle
# Draw Right-angle Triangle by side lengths [a, b] (calculates own C)
triangle = [10, 15]
line_width = 2

coord_origin = (10, 10)
coord_a = (coord_origin[0]+triangle[0], coord_origin[1],)
coord_b = (coord_a[0], coord_origin[1]+triangle[1])

# Canvas
canvas = tkinter.Canvas(window)


canvas.pack()

# Present
window.mainloop()