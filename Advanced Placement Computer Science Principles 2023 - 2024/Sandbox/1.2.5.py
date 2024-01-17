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
wordlist= ["import hack-terminal", "ip = get(ip)", "var = 3.141592654", "def hackComputer(u-ip): \n print(u-ip) \n u-ip.getUserData()", "x = hex(255)", "# This is a python comment", "import turtle as trtl \n painter = trtl.Turtle() \n painter.forward() \n wn = trtl.Screen() \n wn.mainloop()", "Hijack can't say that in an airport"]
returns = [1,1,1,3,1,1,5,1]
random = []
def init():
global var
var = None
for i in range(100):
choose = rand.randrange(len(wordlist))
random.append(choose)
print(random)
return random








#gets rid of letters when typed
#letter gone code
storage = [1]
def hackerman():
var = -1
myStore = ""
for k in range(len(storage)):
var = var + 1
myStore = storage[var]
myChoice = random[myStore]
myChoice1 = random[myStore + 1]
space = 20*int(returns[myChoice1])
y = drawer.ycor()-space
drawer.write( wordlist[myChoice], font=("Arial", 16, "bold"))
print(y)
drawer.goto(-700, y)
myStore = myStore + 1
storage.append(myStore)
print(storage)
return storage


init()




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






