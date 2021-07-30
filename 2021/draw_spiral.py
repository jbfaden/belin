# How would you make a...
#  ... triangle?
#  ... pentagon?
#  ... star?

import turtle as t

def draw_shape(size, num_sides, angle):
    """size is length of each side, num_sides is the number of sides, and angle is the amount to turn"""
    t.pendown()
    for i in range(num_sides):
        t.forward(size)
        t.left(angle)
    t.penup()

size = 20
for _ in range(120):
    draw_shape(size, 6, 60)
    size = size * 0.99

t.done()
