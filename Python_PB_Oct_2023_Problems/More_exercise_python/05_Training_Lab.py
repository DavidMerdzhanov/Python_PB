

workplace_desk_width = 70
workplace_desk_height = 120
corridor_width = 100
entrance_door_width = 160  # загуба на 1 работно  място
podium_height = 160  # загуба на 2 работни места
podium_width = 120  # загуба на 2 работни места


height = float(input())       # дължина на залата в метри
width = float(input())        # широчина на залата в метри

height_in_centimeters = height * 100   #преобразуваме в сантиметри
width_in_centimeters = width * 100


total_width = width_in_centimeters - corridor_width
col = total_width // workplace_desk_width

rows = height_in_centimeters // workplace_desk_height


number_of_seats = (col * rows) - 3

print(f"{number_of_seats}")

