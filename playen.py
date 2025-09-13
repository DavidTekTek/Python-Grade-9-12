import math

# Ask the user what shape they want
shape = input("Enter the shape you want to calculate the area for: ")

# Check if the user typed SPHERE or sphere
if shape == "SPHERE" or shape == "sphere":
    radius = float(input("Enter the radius of the sphere: "))
    area = 4 * math.pi * radius ** 2   # formula for area of a sphere
    print("The area of the sphere is:", area)
else:
    print("This program only calculates the area of a sphere.")
