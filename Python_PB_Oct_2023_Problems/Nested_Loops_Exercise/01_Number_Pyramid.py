

number = int(input())

current = 1
is_current_bigger_then_n = False

for row in range(1, number + 1):
    for col in range(1, row + 1):

        if current > number:
            is_current_bigger_then_n = True
            break
     


