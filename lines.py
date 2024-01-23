#!/usr/bin/env python
import tkinter

# Window Properties
window = tkinter.Tk()
window.geometry("800x600")
window.minsize(400, 300)
window.title("Drawing Lines :p")

# Triangle
# Draw Right-angle Triangle by side lengths [a, b] (calculates own C)
triangle = [500, 250]
line_width = 2

coord_origin = (5, 5)
coord_a = (coord_origin[0]+triangle[0], coord_origin[1],)
coord_b = (coord_a[0], coord_origin[1]+triangle[1])

# Canvas
canvas = tkinter.Canvas(window)

canvas.create_line(*coord_origin, *coord_a, width=line_width)
canvas.create_line(*coord_origin, *coord_b, width=line_width)
canvas.create_line(*coord_b, *coord_a, width=line_width)

canvas.pack()

# Present
window.mainloop()