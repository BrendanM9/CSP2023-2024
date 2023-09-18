import turtle as trtl

painter = trtl.Turtle()

print("making a circle....")

color = (input("What color?"))

radius = (int(input("What radius?")))

painter.color(color)
painter.circle(radius,360)

wn = trtl.Screen()
wn.mainloop()