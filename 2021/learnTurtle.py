# See https://realpython.com/beginners-guide-python-turtle/
import turtle as t

t.penup()
t.circle(10)
t.forward(20)

for i in range(100):
    t.circle(10)
    t.forward(20)
    t.left(10)
