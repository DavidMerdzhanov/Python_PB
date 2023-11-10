
number = int(input())


for special_numbers in range(1111, 10_000):
    number_to_str = str(special_numbers)

    is_special = True

    for i, digit in enumerate(number_to_str):
        digit_to_int = int(digit)

        if digit_to_int == 0:
            is_special = False
            break

        if number % digit_to_int != 0:
            is_special = False
            break

    if is_special:
        print(f"{special_numbers}", end=" ")

