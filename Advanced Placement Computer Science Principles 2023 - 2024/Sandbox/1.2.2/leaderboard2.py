# set the levels of scoring
bronze_score = 15
silver_score = 20
gold_score = 25


# return names in the leaderboard file
def get_names(file_name, leader_names, leader_scores):
    leaderboard_file = open(file_name, "r")

    # use a loop to iterate through the content of the file, one line at a time
    # note that each line in the file has the format "leader_name, leader_score" for example "Pat,50"
    for line in leaderboard_file:
        leader_name = ""
        leader_score = ""
        index = 0
        # TODO 1: use a while loop to read the leader name from the line (format is "leader_name,leader_score")
        while (line[index] != ","):
            leader_name = leader_name + line[index]
            index = index + 1
        # TODO 2: add the player name to the names list
        leader_names.append(leader_name)
        index = index + 1
        while (line[index] != "\n"):
            leader_score = leader_score + line[index]
            index = index + 1
        # TODO 6: return the names list in place of the empty list
            leader_scores.append(int(leader_score))
    leaderboard_file.close()
    #return names
# return scores from the leaderboard file
'''def get_scores(file_name):
    leaderboard_file = open(file_name, "r")
    global scores
    scores = []
    for line in leaderboard_file:
        leader_score = ""
        index = 0
        # TODO 3: use a while loop to index beyond the comma, skipping the player's name
        while (line[index] != ","):
            pass
        while (line[index] != "\n"):
            leader_score = leader_score + line[index]
            index = index + 1
        # TODO 4: use a while loop to get the score
            leader_score.append(leader_score)
        # TODO 5: add the player score to the scores list
    leaderboard_file.close()
    # TODO 7: return the score in place of the empty list
    return scores'''
# update leaderboard by inserting the current player and score to the list at the correct position
def update_leaderboard(file_name, leader_names, leader_scores, player_name, player_score):
    index = 0
    # TODO 8: loop through all the scores in the existing leaderboard list
    #leaderboard_file = file_name
    leader_index = 0
    while (leader_index , len(leader_scores)):
        if (player_score >= leader_scores[leader_index]):
            break
        else:
            leader_index = leader_index + 1
        leader_scores.insert(leader_index, player_score)
        leader_names.insert(leader_index, player_name)
        if (len(leader_names) == 6): 
            leader_names.pop(5)
        if (len(leader_scores)):
            leader_scores.pop(5)
        # TODO 10: insert new player and score

        # TODO 11: keep both lists at 5 elements only (top 5 players)
  
        # TODO 12: store the latest leaderboard back in the file
        leaderboard_file = open(file_name, "w")
        leader_index = 0
        # TODO 13: loop through all the leaderboard elements and write them to the file
        while ():
            leaderboard_file.write(leader_names[leader_index] + "," + str(leader_scores[leader_index]) + "\n")
            leader_index = leader_index + 1
        leaderboard_file.close()
        
# draw leaderboard and display a message to player
def draw_leaderboard(high_scorer, leader_names, leader_scores, turtle_object, player_score):
    #clear the screen and move the turtle object to (-200, 100) to start drawing the leaderboard
    font_setup = ("Arial", 20, "normal")
    turtle_object.clear()
    turtle_object.penup()
    turtle_object.goto(-160, 100)
    turtle_object.hideturtle()
    turtle_object.down()
    # loop through the lists and use the same index to display the corresponding name and score, separated by a tab space '\t'
    for index in range(len(leader_names)):
        turtle_object.write(str(index+1) + "\t" + leader_names[index] + "\t" + str(leader_scores[index]), font= font_setup)
        turtle_object.penup()
        turtle_object.goto(-160, int(turtle_object.ycor()))
        turtle_object.down()
    # move turtle to a new line
    turtle_object.penup()
    turtle_object.goto(-160, int(turtle_object.ycor())-50)
    turtle_object.pendown()
    # TODO 14: display message about player making/not making leaderboard
    if(player_score > leader_scores[4]):
        turtle_object.write("Congratulations!\nYou made the leaderboard!", font=font_setup)
    else:
        turtle_object.write("Sorry!\nYou didn't make the leaderboard.\nMaybe next time!", font=font_setup)
    # move turtle to a new line
    turtle_object.penup()
    turtle_object.goto(-160, int(turtle_object.ycor())-50)
    turtle_object.pendown()
    # TODO 15: Display a gold/silver/bronze message if player earned a gold/silver/or bronze medal; display nothing if no medal
    if(leader_scores >= gold_score):
        turtle_object.write("You earned a gold medal!", font=font_setup)
    elif(leader_scores >= silver_score and leader_scores <gold_score):
        turtle_object.write("You earned a silver medal!", font=font_setup)
    elif(leader_scores >= bronze_score and leader_scores < silver_score):
        turtle_object.write("You earned a bronze medal!", font=font_setup)