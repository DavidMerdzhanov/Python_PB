width_of_cake = int(input())
length_of_cake = int(input())

cake_total = width_of_cake * length_of_cake
cake_left = cake_total
command = input()
while command != "STOP":
    number_of_cake_piece = int(command)
    cake_left -= number_of_cake_piece
    if cake_left <= 0:
        break

    command = input()

if command == "STOP":
    print(f"{cake_left} pieces are left.")
else:
    cake_pieces_needed = -cake_left
    print(f"No more cake left! You need {cake_pieces_needed} pieces more.")
