#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
x = trtl.Turtle()
x.pensize(40)
x.circle(20)
legs = 8
y = 90
angle = 360 / legs -10
x.pensize(5)
n = 0
for i in range(2):
    while (n < legs/2):
        x.goto(0,0)
        x.setheading(angle*n)
        x.forward(y)
        n = n + 1
    x.setheading(angle*i)
x.hideturtle()
wn = trtl.Screen()
wn.mainloop()