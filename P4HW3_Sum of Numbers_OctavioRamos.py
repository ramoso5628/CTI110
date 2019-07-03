# Sum of Numbers
# 1 July 2019
# CTI-110 P4HW3 - Sum of Numbers
# Octavio Ramos

# Write a program with a loop that asks the user to enter a series of positive numbers.
# Enter a negative number to signal the end of the series.
# All positive numbers have been entered, the program should display their sum.

total = 0
userNumber = float( input("Enter the first number or a negative number to quit: " ))

while userNumber > -1:
    total = total + userNumber
    userNumber = float( input("Enter the next number or a negative number to quit:" ))

    
print("The sum of all you numbers you entered is", total)
