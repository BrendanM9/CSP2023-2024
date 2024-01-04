import random as r
wordssssssssssssssss = ["a", "b", "c", "d", "e", "f", "g"]
wordlist = []
linelist = []
lineHeight = 20
class codeLines:
    a = ["import hack-terminal", 1]
    b = ["ip = get(ip)", 1]
    c = ["var = 3.141592654", 1]
    d = ["def hackComputer(u-ip): \n print(u-ip) \n u-ip.getUserData()",3]
    e = ["x = hex(255)", 1]
    f = ["# This is a python comment", 1]
    g = ["import turtle as trtl \n painter = trtl.Turtle() \n painter.forward() \n wn = trtl.Screen() \n wn.mainloop()",5]

        
print(len(wordssssssssssssssss))
for i in range(len(wordssssssssssssssss)):
    number1 = wordssssssssssssssss[r.randrange(len(wordssssssssssssssss))]
    measure = 0
    if(number1 == "a"):
        line = codeLines.a[0]
        measure = codeLines.a[1]
    elif(number1 == "b"):
        line = codeLines.b[0]
        measure = codeLines.b[1]
    elif(number1 == "c"):
        line = codeLines.c[0]
        measure = codeLines.c[1]
    elif(number1 == "d"):
        line = codeLines.d[0]
        measure = codeLines.d[1]
    elif(number1 == "e"):
        line = codeLines.e[0]
        measure = codeLines.e[1]
    elif(number1 == "f"):
        line = codeLines.f[0]
        measure = codeLines.f[1]
    elif(number1 == "g"):
        line = codeLines.g[0]
        measure = codeLines.g[1]
    print(line)
    wordlist.append(line) 
    linelist.append(measure)
    #imported stuff
import turtle as trtl
import random as rand 
from time import sleep as sl






#setup for turtles
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
drawer = trtl.Turtle()
drawer.penup()
drawer.hideturtle()
wn.bgcolor("black")
drawer.color("green")
drawer.goto(-700, 350)




#words
#wordlist= ["import hack-terminal", "ip = get(ip)", "var = 3.141592654", "def hackComputer(u-ip): \n print(u-ip) \n u-ip.getUserData()", "x = hex(255)", "# This is a python comment", "import turtle as trtl \n painter = trtl.Turtle() \n painter.forward() \n wn = trtl.Screen() \n wn.mainloop()", "Hijack can't say that in an airport"]




#gets rid of letters when typed
#letter gone code
global iterate
iterate = 0
def hackerman():
    drawer.write(wordlist[iterate], font=("Arial", 16, "bold"))
    drawer.forward(linelist[iterate])
    i = i + 1




wn.update()




wn.listen()






#typing that activates lettergone code
wn.onkeypress(hackerman, "a")
wn.onkeypress(hackerman, "b")
wn.onkeypress(hackerman, "c")
wn.onkeypress(hackerman, "d")
wn.onkeypress(hackerman, "e")
wn.onkeypress(hackerman, "f")
wn.onkeypress(hackerman, "g")
wn.onkeypress(hackerman, "h")
wn.onkeypress(hackerman, "i")
wn.onkeypress(hackerman, "j")
wn.onkeypress(hackerman, "k")
wn.onkeypress(hackerman, "l")
wn.onkeypress(hackerman, "m")
wn.onkeypress(hackerman, "n")
wn.onkeypress(hackerman, "o")
wn.onkeypress(hackerman, "p")
wn.onkeypress(hackerman, "q")
wn.onkeypress(hackerman, "r")
wn.onkeypress(hackerman, "s")
wn.onkeypress(hackerman, "t")
wn.onkeypress(hackerman, "u")
wn.onkeypress(hackerman, "v")
wn.onkeypress(hackerman, "w")
wn.onkeypress(hackerman, "x")
wn.onkeypress(hackerman, "y")
wn.onkeypress(hackerman, "z")
wn.onkeypress(hackerman, "Q")
wn.onkeypress(hackerman, "W")
wn.onkeypress(hackerman, "E")
wn.onkeypress(hackerman, "R")
wn.onkeypress(hackerman, "T")
wn.onkeypress(hackerman, "Y")
wn.onkeypress(hackerman, "U")
wn.onkeypress(hackerman, "I")
wn.onkeypress(hackerman, "O")
wn.onkeypress(hackerman, "P")
wn.onkeypress(hackerman, "A")
wn.onkeypress(hackerman, "S")
wn.onkeypress(hackerman, "D")
wn.onkeypress(hackerman, "F")
wn.onkeypress(hackerman, "G")
wn.onkeypress(hackerman, "H")
wn.onkeypress(hackerman, "J")
wn.onkeypress(hackerman, "K")
wn.onkeypress(hackerman, "L")
wn.onkeypress(hackerman, "Z")
wn.onkeypress(hackerman, "X")
wn.onkeypress(hackerman, "C")
wn.onkeypress(hackerman, "V")
wn.onkeypress(hackerman, "B")
wn.onkeypress(hackerman, "N")
wn.onkeypress(hackerman, "M")
wn.onkeypress(hackerman, " ")
wn.onkeypress(hackerman, "0")
wn.onkeypress(hackerman, "1")
wn.onkeypress(hackerman, "2")
wn.onkeypress(hackerman, "3")
wn.onkeypress(hackerman, "4")
wn.onkeypress(hackerman, "5")
wn.onkeypress(hackerman, "6")
wn.onkeypress(hackerman, "7")
wn.onkeypress(hackerman, "8")
wn.onkeypress(hackerman, "9")






#screen setup
wn = trtl.Screen()
wn.mainloop()
#—-------------------------------------------------------------------------------------
