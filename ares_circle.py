import math

# Prompt the user to enter the radius
radius = float(input("Enter the radius of the circle: "))

# Calculate the area of the circle
area = math.pi * (radius ** 2)

# Display the result
print(f"The area of the circle with radius {radius} is {area:.2f}")

# Prompt the user to enter the length of a side of an equilateral triangle
side_length = float(input("Enter the length of a side of an equilateral triangle: "))

# Calculate the area of the equilateral triangle
triangle_area = (math.sqrt(3) / 4)  (side_length ** 2)
print(f"The area of the equilateral triangle with side length {side_length} is {triangle_area:.2f}")
