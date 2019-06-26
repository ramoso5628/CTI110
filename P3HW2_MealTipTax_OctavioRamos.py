# CTI-110 
# P3HW2 - MealTipTax 
# Octavio Ramos
# 25 June 2019
#

# Have the user enter the charge of the meal.
# Ask the user to enter the tip percentage they would like to consider
#(15% or 18% or 20%),if the user enters another percentage, the program is to display and error.
# The program is to display all of these amounts (tip, tax, and total).


# User will enter the cost of the meal.
meal = float(input('Enter meal cost #: '))

# User will enter the sales tax by decimal.
tax = float(input('Enter tax price #: '))

# User will enter tip by decimal.
tip = float(input('Enter tip amount #: '))

meal = meal + meal * tax
meal = meal + meal * tip

total = meal

print("Total cost of meal:$ %.2f" % total)




