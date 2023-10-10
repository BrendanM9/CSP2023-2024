#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]
startx = 0
starty = 0

for c in range(len(turtle_colors)):
  t = trtl.Turtle()
  t.speed(0)
  t.color(turtle_colors[c])
  t.penup()
  t.goto(startx, starty)
  t.pendown()
  my_turtles.append(t)
  t.shape(turtle_shapes[c])
'''
for i in turtle_colors:
    t.color(i)
#  
'''

#
for t in my_turtles:
  t.goto(startx-t.xcor(), starty-t.ycor())
  t.right(45)     
  t.forward(50)
  startx = startx+50
  starty = starty+50

#	
  

wn = trtl.Screen()
wn.mainloop()