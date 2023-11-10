import math

kind_figure = input()
side_1 = float(input())

if kind_figure == "square":
    area_of_square = side_1 * side_1
    print(f"{area_of_square: .3f}")
elif kind_figure == "rectangle":
    side_2 = float(input())
    area_of_rectangle = side_1 * side_2
    print(f"{area_of_rectangle: .3f}")
elif kind_figure == "circle":
    area_of_circle = math.pi * side_1 ** 2
    print(f"{area_of_circle: .3f}")
elif kind_figure == "triangle":
    side_2 = float(input())
    area_of_triangle = side_1 * side_2 / 2
    print(f"{area_of_triangle: .3f}")
