
number = int(input())
combination_count = 0
for x in range(0, number + 1):
    for x2 in range(0, number + 1):
        for x3 in range(0, number + 1):
            if x + x2 + x3 == number:
                combination_count += 1

print(combination_count)


