# Length and Width Of Two Rectangles
# 24 June 2019
# CTI-110 P3T1 - Area of Rectangles
# Octavio Ramos
#

# Input the length and width of rectangle 1.
length1 = int(input('Enter the length of rectangle 1: '))
width1 = int(input('Enter the width of rectangle 1: '))

# Input the length and width of rectangle 2.
length2 = int(input('Enter the length of rectangle 2: '))
width2 = int(input('Enter the width of rectangle 2: '))

# Calculate the area of rectangle 1.
area1 = length1 * width1
area2 = length2 * width2

# Both rectangles have equal area.
if area1 > area2:
    print('Rectangle 1 has the larger area.')
elif area2 > area1:
    print('Rectangle 2 has the larger area.')
else:
    print('Both Rectangles have equal area.')
            
