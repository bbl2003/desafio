# This function calculates the area of a triangle.
def triangle_area(base, height):
    total_area = (base * height)/2
    return total_area


base = int(input("Enter the base of the triangle: "))
height = int(input("Enter the height of the triangle: "))
area = triangle_area(base, height)
print(f"The area of the triangle is: {area}")