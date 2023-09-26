import turtle as trtl

color1 = "white"
color2 = "orange"

wn = trtl.Screen()
height = 500

painter = trtl.Turtle()
painter.speed(0)
painter.color(color1)
painter.pensize(5)
trtl.bgcolor("black")

space = 1
angle = 65
seg = int(painter.ycor()/angle)

while (painter.ycor() < height):
    if(space % 2 == 0):
        painter.fillcolor(color1)
        painter.color(color1)
    elif(space % 2 == 1):
        painter.fillcolor(color1)
        painter.color(color1)

    painter.right(angle)
    painter.forward(2*space + 10)
    painter.begin_fill()
    painter.circle(3)
    painter.end_fill()
    space += 1

wn.mainloop()    