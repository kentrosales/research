#Calculating area of composite shapes
def calculate_composite_area(s, g, q, w):
    total_rectangle = s * g
    cutout_rectangle = q * w
    blue_area = total_rectangle - cutout_rectangle
    return blue_area
#assign values to variables
s = 10
g = 8
q = 5
w = 3
result = calculate_composite_area(s, g, q, w)
#display result
print(f"The area of the blue part of the rectangle is {result}")
#assertion
#Area of Blue Part = 65 using formula [Total rectangle - cutout Rectangle]
   
