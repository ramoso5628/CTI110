# Paper, Rock, Scissor Game 
# 9 July 2019
# CTI-110 P5HW2-Paper, Rock, Scissor Game
# Octavio Ramos


# Write a program that lets you play the rock, paper, scissor game against the computer.




from random import randint

#create a list of play options
t = ["rock", "paper", "scissor"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    player = input("rock, paper, scissor? ")
    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "paper":
        if computer == "scissor":
            print("You lose!", computer, "cuts", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "scissor":
        if computer == "rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cuts", computer)
    else:
        print("Pay attention!  Look at the spelling and don't cap. !")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]
