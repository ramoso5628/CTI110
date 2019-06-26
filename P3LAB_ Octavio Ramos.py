# P3LAB Debugging
# CTI-110
# 25 June 2019
# Octavio Ramos
# This lab will be used to calculate students grades





# User will enter a numeric grade.
# The numeric grade is given in a letter grade.

def main():
    grade = int(input("Enter a numeric grade:"))
    if grade >=90:
       print("You made an A")
    elif grade > 79 and grade < 90:
       print("You made an B")
    elif grade > 69:
       print("You made a C")
    elif grade > 59:
       print("You made a D")
    else:
       print("You made an F")
                
main()
