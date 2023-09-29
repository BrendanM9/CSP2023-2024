#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
x = trtl.Turtle()
x.pensize(40)
x.circle(20)
legs = 8
y = 70
angle = 380 / legs
x.pensize(5)
n = 0
while (n < legs):
  x.goto(0,0)
  x.setheading(angle*n)
  x.forward(y)
  n = n + 1
x.hideturtle()
wn = trtl.Screen()
wn.mainloop()