import math

def get_triangle_area(d, e):
    # Validation: The hypotenuse (e) must be longer than the base (d)
    if e <= d: #if e is shorter, it will display an error
        return "Error: The hypotenuse 'e' must be longer than the base 'd'."
    # Step 1: Calculate the vertical height using Pythagoras
    height = math.sqrt(e**2 - d**2)
    # Step 2: Calculate the area
    area = 0.5 * d * height
    return area
#example value given
d = 9
e = 21

print("The area of the given shape is", (get_triangle_area(d, e)))