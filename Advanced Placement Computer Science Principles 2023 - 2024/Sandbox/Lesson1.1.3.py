import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)

painter.color("green")
painter.pensize(15)
painter.goto(0,-150)
painter.setheading(90)
painter.forward(100)

painter.setheading(270)
painter.circle(20,120,20)
painter.setheading(90)
painter.goto(0,-60)

painter.forward(60)
painter.setheading(0)

painter.penup()
painter.shape("circle")
painter.turtlesize(2)

painter.goto(20,180)

for petal in range(18):
    painter.right(20)
    painter.forward(30)
    painter.color("darkorchid")
    rem = petal % 2
    if (rem == 0):
        painter.color("blue")
    painter.stamp()

painter.goto(20,150)

for petal in range(12):
    painter.right(30)
    painter.forward(30)
    painter.color("blue")
    rem = petal % 2
    if (rem == 0):
        painter.color("darkorchid")
    painter.stamp()

painter.goto(20,120)
painter.color("yellow")

for petal in range(6):
    painter.right(60)
    painter.forward(30)
    painter.stamp()
wn = trtl.Screen()
wn.mainloop()