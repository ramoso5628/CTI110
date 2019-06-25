# CTI-110
# 24 June 2019
# P3HW1 - Color Mixer
# Octavio Ramos
# 24 June 2019
#

# Color Mixer Lab
# Colors are red, blue, and yellow are the primary colors and
# cannot be made by mixing any other colors.  When you mix two primary colors
# you get a secondary color.
# When you mix red and blue, you get purple.
# When you mix red and yellow, you get orange.
# When you mix red and yellow, you get green.
# Design a program that prompts the user to enter the names of two primary
# colors to mix. If the user is prompted to enter anything other than "red"
# "blue," or "yello," the program will display error message.  Otherwise, the
# program should display the name of the secondary color that results.

primarycolor1 = input('Choose your first color. (red, blue, yellow) :')
primarycolor2 = input('What is your second color? (red, blue, yellow) :')

if primarycolor1 == 'red' and primarycolor2 == 'blue' or primarycolor1 == 'blue' and primarycolor2 == 'red':
    print('Your result is purple')
elif primarycolor1 == 'red' and primarycolor2 == 'yellow' or primarycolor1 == 'yellow' and primarycolor2 == 'red':
    print('Your result is orange')
elif primarycolor1 == 'blue' and primarycolor2 == 'yellow' or primarycolor1 == 'yellow' and primarycolor2 == 'blue':
    print('Your result is green')
