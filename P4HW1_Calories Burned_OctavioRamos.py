# Calories burned in one minute
# 1 July 2019
# CTI-110 P4HW1 - Calories Burned
# Octavio Ramos

# This program will calculate the amout of calories burned.
# Assuming you burn 5 calories per minute.

time = int(input('How many minutes were you exercising? '))

calories = 0  
for i in range(time):
    calories += 5

print('You burned {} calories'.format(calories))
    
