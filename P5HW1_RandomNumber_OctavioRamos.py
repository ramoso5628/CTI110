# Random Number
# 9 July 2019
# CTI-110 P5HW1- Random Number
# Octavio Ramos

# Write a program that generates a random number in the range of 1 to 100, and
# ask the user to guess what number it is.  If the user's gues is higher than the
# random, the program should display "Too high, try again," if lower random number
# the program should display "Too low, try again."  If the random number is guessed
# the application shouls congratulate the user and generate a new random number.

import random
random_number = random.randint(1,100)
win = False
Turns =0
while win==False:
    Your_guess = input("Enter a number between 1 and 100 and GOOD LUCK! ")
    Turns +=1
    if random_number==int(Your_guess):
        print("You GUESSED CORRECTLY!!")
        print("Number of GUESSES you have used: ",Turns)
        win == True
        break
    else:
     if random_number>int(Your_guess):
        print("Your guess was low, Please enter a higher number ")
     else:
        print("your guess was high, please enter a lower number ")
