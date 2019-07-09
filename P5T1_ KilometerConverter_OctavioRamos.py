# Kilometer Converter
# 9 July 2019
# CTI-110 P55T1- Kilometer Converter
# Octavio Ramos

# This program will tell the user to input a kilometer distant and it will convert into miles.
# The conversion formula is the folling Miles = Kilometers x 0.6214

conversion_factor = 0.6214

def main():
    
    kilometers = float(input("Enter a distance in kilometers: "))

    show_miles(kilometers)

def show_miles(km):
    
    miles = km * conversion_factor
    print(km, "kilomters equals to",format(miles,".2f"),"miles.") 


main()
