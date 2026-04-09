import math

def calculate_blue_area(radius):
    full_area = math.pi * (radius ** 2)
    blue_area = 0.75 * full_area
    return blue_area
radius = 5
print(f"The area of Pacman is", (int(round(calculate_blue_area(radius)))))