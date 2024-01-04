import turtle as trtl
import random as randomNo
import leaderboard as lb
leaderboard_file_name = "a122_leaderboard.txt"
player_name = input("What is your name?")
painter = trtl.Turtle()
painter.shape("turtle")
score = 0
x = 0
y = 0
leader_names_list = []
leader_scores_list = []
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000
timer_up = False
counter = trtl.Turtle()
point = trtl.Turtle()
point.penup()
point.goto(250,250)
counter.penup()
counter.goto(-250,250)
def manage_leaderboard():
    global score
    global painter
    leader_names_list = lb.get_names(leaderboard_file_name)
    leader_scores_list = lb.get_scores(leaderboard_file_name)
    if(len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
        lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
        lb.draw_leaderboard(True, leader_names_list, leader_scores_list, painter, score)
    else:
        lb.draw_leaderboard(False, leader_names_list, leader_scores_list, painter, score)
def addpoint():
    global score
    score = score + 1
    print(score)
    point.clear()
    point.write("Score: "+ str(score), font=font_setup)
def spot_clicked(x, y):
    #print("You Clicked Me!")
    painter.penup()
    x = randomNo.randrange(-200, 200)
    y = randomNo.randrange(-200, 200)
    painter.goto(x, y)
    addpoint()
    
def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up", font = font_setup)
        timer_up = True
        manage_leaderboard()
        painter.hideturtle()
    else:
        counter.write("Timer: "+ str(timer), font=font_setup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval)


wn = trtl.Screen()
painter.onclick(spot_clicked)
wn.ontimer(countdown, counter_interval)
wn.mainloop()