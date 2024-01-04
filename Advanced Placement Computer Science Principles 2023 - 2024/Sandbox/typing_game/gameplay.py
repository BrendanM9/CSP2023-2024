import leaders as lb
names1 = []
recieves1 = []
name1 = input("What is your name?")
recieve1 = int(input("What is your score?"))
myFile = "leaderscores.txt"
names1 = lb.recieve_name(myFile)
recieves1 = lb.recieve_accuracy(myFile)
lb.update_leaders(myFile, names1, recieves1, name1, recieve1)