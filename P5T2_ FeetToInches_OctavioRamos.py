# Feet to Inches
# 9 July 2019
# CTI-110 P55T2- Feet to Inches
# Octavio Ramos

# One foot equals 12 inches.
# Write a program that will take a number of feet as an arguement and returns the number in inches
# The user will be prompted to add the number in feet and the result will display in inches.

inches_per_foot = 12

def main():
    
    feet = int(input("Enter a number of feet: "))

    print(feet, "equals to", feet_to_inches(feet), "inches.")
    

def feet_to_inches(feet):
    return feet * inches_per_foot

main()
