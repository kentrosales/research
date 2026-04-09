import math 
def calculate_total_area(e):
    g = e #g is a radius of e
    
    # 1. Area of the Semicircle
    # formula for getting area of circle = math.pi * (radius ** 2)
    area_semicircle = 0.5 * math.pi * (e**2)
    
    # 2. Area of the Triangle
    # We need the base 'b'. tan(38 degrees) = g / b  =>  b = g / tan(38)
    angle_rad = math.radians(38)
    base_triangle = g / math.tan(angle_rad)
    area_triangle = 0.5 * base_triangle * g
    
    # 3. Total Area
    total_area = area_semicircle + area_triangle
    return total_area
#give value to variable "e"
e_value= 10  # write "value" after e so no accidents in code
result = calculate_total_area(e_value)

print(result)