import turtle as trtl
import random as random1

painter = trtl.Turtle()
#get a size
drawsize = int(input("What size? (0-100)"))
#different types of lists
turtlecolor1 = ["red", "green", "purple"]
turtlecolor2 = ["blue", "orange", "gold"]
painter.pensize(drawsize/2)
painter.speed(0)
#chooses color list based on pen size
if(drawsize >= 0 and drawsize <= 50):
    trtl.Screen().bgcolor(turtlecolor2[0])
    for l in range (764):
        for i in turtlecolor1:
            painter.pencolor(i)
            painter.left(50)
            painter.forward(50+l)
        print(l)
elif(drawsize > 50 and drawsize <=100):
    trtl.Screen().bgcolor(turtlecolor1[0])
    for r in range(764):
        for a in turtlecolor2:
            painter.pencolor(a)
            painter.left(50)
            painter.forward(50+r)
            
        print(r)
painter.goto(0,0)
painter.write("I don't trust stairs. They're always up to something.")
wn = trtl.Screen()
wn.mainloop()