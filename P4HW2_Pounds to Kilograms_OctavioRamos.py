# Create Pounds to Kilograms by creating a table startinmg at 100lbs to 300lbs
# 1 July 2019
# CTI-110 P4HW1 - Pounds to Kilograms
# Octavio Ramos

#1.) Declare the variables
#  Kilos =  (Pounds / 2.2046)
#2.) Print the table headers
#3.) Set the loop in range 100lbs-300lbs in increments of 10
#4.) Display the table 


print (" Kilos     \t       Pounds")
print ("-------------------------------")

for Pounds in range (100, 301, 10):
    Kilos = (Pounds / 2.2046)
    print (Kilos, '\t', Pounds)
