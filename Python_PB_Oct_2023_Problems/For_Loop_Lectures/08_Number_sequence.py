import sys

count_numbers = int(input())

max_number = -sys.maxsize
min_number = sys.maxsize


for number in range(count_numbers):
    add_number = int(input())
    if add_number > max_number:
        max_number = add_number
    if add_number < min_number:
        min_number = add_number

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")




