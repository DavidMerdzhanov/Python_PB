

number = int(input())

left_numbers = 0
right_numbers = 0


for num in range(number * 2):
    sum_numbers = int(input())
    if num < number:
        left_numbers += sum_numbers

    else:
        right_numbers += sum_numbers


if left_numbers == right_numbers:
    print(f"Yes, sum = {left_numbers}")

else:
    difference = abs(left_numbers - right_numbers)
    print(f"No, diff = {difference}")


