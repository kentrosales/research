# base = k
#height = j

def calculate_triangle_area(base, height):
    area = 0.5 * (base * height)
    return area
k = 10
j = 5
triangle_area = calculate_triangle_area(k, j)
print(f"The area of the triangle with a base(k): {k} and height(j): {j} is {triangle_area}")
