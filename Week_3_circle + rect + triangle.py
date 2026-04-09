import math

def calculate_total_area(e, f, g):
    radius = g / 2
    area_semicircle = 0.5 * math.pi * (radius ** 2)
    rectangle = e * g
    triangle = 0.5 * f * g
    total_area = area_semicircle + rectangle + triangle
    return total_area
# Assign values to variable (we use (_val) to not accidentally break the variables e, f, g)
e_val = 2
f_val = 8
g_val = 8

area = calculate_total_area(e_val, f_val, g_val)
print(f"The total area of the hybrid shape is", (int(calculate_total_area(e_val, f_val, g_val))))
#Assertion:
#all the formula of the shapes that have been "fused" will determine the final result
