import math

def regular_polygon_area(number_of_sides, length_of_side):
    return (1.0 / 4.0 * number_of_sides * length_of_side ** 2 / math.tan(math.pi / number_of_sides))

print regular_polygon_area(7, 3)
