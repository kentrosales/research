import math

def calculate_triangle_area(base_f):
    angle_degrees = 40
    #Calculate radians using given degree angle
    angle_radians = math.radians(angle_degrees)
    # 2. Calculate height using tan(40) = height / base
    # height = base * tan(40)
    height = base_f * math.tan(angle_radians)
    # 3. Calculate area (1/2 * base * height)
    # 0.5 since a triangle is basically a half rectangle
    area = 0.5 * base_f * height
    return area
# Example: If f = 10
base_f = 10
result = calculate_triangle_area(base_f)
print(result)