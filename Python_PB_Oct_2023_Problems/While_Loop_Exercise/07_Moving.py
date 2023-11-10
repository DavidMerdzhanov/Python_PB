
width_free_space = int(input())
length_free_space = int(input())
height_free_space = int(input())

total_space = width_free_space * length_free_space * height_free_space
free_space = total_space

command = input()
while command != "Done":
    number_of_cartons = int(command)
    free_space -= number_of_cartons
    if free_space <= 0:
        break
    command = input()


if command == "Done":
    print(f"{free_space} Cubic meters left.")
else:
    space_needed = -free_space
    print(f"No more free space! You need {space_needed} Cubic meters more.")

