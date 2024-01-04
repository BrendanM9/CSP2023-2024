def recieve_name(file_name):
    leaderboard_file = open(file_name, "r")
    names = []
    for line in leaderboard_file:
        leader_name = ""
        index = 0
        while(line[index] != ","):
            leader_name = leader_name + line[index]
            index = index + 1
        names.append(leader_name)
    print("names", names)
    leaderboard_file.close()
    return names
def recieve_accuracy(file_name):
    leaderboard_file = open(file_name, "r")
    accuracies = []
    for line in leaderboard_file:
        leader_accuracy = ""
        index = 0
        while(line[index] != ","):
            index = index + 1
        index = index + 1
        while(line[index] != "\n"):
            leader_accuracy = leader_accuracy + line[index]
            index = index + 1
        accuracies.append(int(leader_accuracy))
    print("Accuracies", accuracies)
    leaderboard_file.close()
    return accuracies
def update_leaders(file_name, leader_names, leader_accuracy, player_name, player_accuracy):
    print(leader_accuracy)
    for index in range(len(leader_accuracy)):
        if (player_accuracy >= leader_accuracy[index]):
            break
        else:
            index = index + 1
    leader_names.insert(index, player_name)
    leader_accuracy.insert(index, player_accuracy)
    if (len(leader_names) > 5):
        leader_names.pop()
        leader_accuracy.pop()
    leaderboard_file = open(file_name, "w")
    for iterate in range(len(leader_accuracy)):
        if(leader_names[iterate] == player_name):
            if(leader_accuracy[iterate] <= player_accuracy):
                #leader_accuracy.pop()
                print("Testing",leader_accuracy[iterate])
                print(iterate)
                #print(leader_accuracy)
            else:
                for index in range(len(leader_names)):
                    leaderboard_file.write(leader_names[index]+","+ str(leader_accuracy[index])+"\n")
        else:
            for index in range(len(leader_names)):
                leaderboard_file.write(leader_names[index]+","+ str(leader_accuracy[index])+"\n")
    
    leaderboard_file.close()
    