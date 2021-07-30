# This draws the hands of a clock.  This is a 24-hour
# clock.  How do you make it into a 12 am/pm clock?
# Add numbers for the hours!

import time
import turtle as t

now = time.localtime()
print(f"the time is {now.tm_hour}:{now.tm_min}")

# draw the hour hand
t.home()
t.pendown()
t.pensize(10)
t.setheading(90)  # midnight
t.right(now.tm_hour / 24 * 360)
t.forward(200)
t.penup()

t.home()
t.pendown()
t.pensize(5)
t.setheading(90)  # midnight
t.right(now.tm_min / 60 * 360)
t.forward(300)

t.done()
