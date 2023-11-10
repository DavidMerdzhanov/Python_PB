import sys


number = int(input())

max_number = -sys.maxsize
sum_numbers = 0

for i in range(number):
    current_number = int(input())

    if current_number > max_number:
        max_number = current_number

    sum_numbers += current_number


if max_number == sum_numbers - max_number:
    print(f"Yes\n"
          f"Sum = {max_number}")
else:
    diff = abs(max_number - (sum_numbers - max_number))
    print(f"No\n"
          f"Diff = {diff}")


