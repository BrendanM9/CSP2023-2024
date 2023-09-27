import turtle as trtl

ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)

ladybug.penup()
ladybug.goto(0, -55)
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0,5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

while (num_dots <= 2):
    ladybug.penup()
    ladybug.goto(xpos, ypos)
    ladybug.pendown()
    ladybug.circle(3)
    ladybug.penup()
    ladybug.goto(xpos + 30, ypos + 20)
    ladybug.pendown()
    ladybug.circle(2)

    ypos = ypos + 25
    xpos = xpos + 5
    num_dots = num_dots + 1

ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()