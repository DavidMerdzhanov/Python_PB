
door_width = 1.2
door_height = 2
green_paint_per_liter = 3.4
red_paint_per_liter = 4.3
window_side = 1.5


height_of_the_house = float(input())
length_of_the_side_wall = float(input())
height_of_triangular_wall_of_roof = float(input())


side_wall_area = height_of_the_house * length_of_the_side_wall
window = window_side * window_side
both_sides = (2 * side_wall_area) - (2 * window)

back_wall_area = height_of_the_house * height_of_the_house
door = door_width * door_height

front_back_sides = (back_wall_area * 2) - door
total_area = both_sides + front_back_sides

green_paint = total_area / green_paint_per_liter

two_rectangles_on_roof = (height_of_the_house * length_of_the_side_wall) * 2
two_triangles_on_roof = 2 * (height_of_the_house * height_of_triangular_wall_of_roof / 2)
total_are_roof = two_triangles_on_roof + two_rectangles_on_roof

red_paint = total_are_roof / red_paint_per_liter

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")