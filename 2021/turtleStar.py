# this needs to be verified
# How would you make a...
#  ... triangle?
#  ... pentagon?
#  ... star?

import turtle as t

sides = 5
angle = 90
length = 100

while sides > 0:
    t.forward(length)
    t.right(angle)
    sides = sides - 1

