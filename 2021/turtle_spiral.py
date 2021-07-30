import turtle as t


def draw_shape(size, num_sides, angle):
    """size is length of each side, num_sides is the number of sides, and angle is the amount to turn"""
    t.pendown()
    for _ in range(num_sides):
        t.forward(size)
        t.left(angle)
    t.penup()


t.speed(100)
size = 20
for _ in range(20):
    draw_shape(size, 6, 60)
    t.forward(size * 2)
    t.left(10)
    size = size * 0.9

t.done()
