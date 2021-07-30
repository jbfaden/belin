# How would you make a...
#  ... triangle?
#  ... pentagon?
#  ... star?

import turtle as t

sides = 5
angle = 90
length = 100

for _ in range(sides):
    t.forward(length)
    t.right(angle)

t.done()
