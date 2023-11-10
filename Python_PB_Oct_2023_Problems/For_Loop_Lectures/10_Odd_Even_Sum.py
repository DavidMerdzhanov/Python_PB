

number = int(input())

even_position_number = 0
odd_position_number = 0

for num in range(number):
    current_number = int(input())
    if num % 2 == 0:
        even_position_number += current_number
    else:
        odd_position_number += current_number


if even_position_number == odd_position_number:
    print(f"Yes\n"
          f"Sum = {even_position_number}")

else:
    diff = abs(even_position_number - odd_position_number)
    print(f"No\n"
          f"Diff = {diff}")