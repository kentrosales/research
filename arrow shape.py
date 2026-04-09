def calculate_arrow_area(m, u, n):
    rectangle_area = (m * u)
    triangle_area = (0.5 * n * n)
    return rectangle_area + triangle_area
m = 5
u = 8
n = 5
print(f"Arrow_area: {calculate_arrow_area(m, u, n)}")
