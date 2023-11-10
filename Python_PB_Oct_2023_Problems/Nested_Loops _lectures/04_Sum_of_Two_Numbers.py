beginning_number = int(input())
end_number = int(input())
magic_number = int(input())

combination_is_found = False
combination = 0

for first_number in range(beginning_number, end_number + 1):
    for second_number in range(beginning_number, end_number + 1):
        combination += 1
        if first_number + second_number == magic_number:
            combination_is_found = True
            break
    if combination_is_found:
        break

if combination_is_found:
    print(f"Combination N:{combination} ({first_number} + {second_number} = {magic_number})")
else:
    print(f"{combination} combinations - neither equals {magic_number}")
