import math

# Finding the hypotenuse of a right triangle.

# 1. Input both lengths of each side and the code will process and print an output which is your hypotenuse.

sidea = int(input("Enter the length of a: "))
sideb = int(input("Enter the length of b: "))
hypotenuse = math.sqrt(pow(sidea,2) + pow(sideb,2))
print("Your hypotenuse is:", hypotenuse)