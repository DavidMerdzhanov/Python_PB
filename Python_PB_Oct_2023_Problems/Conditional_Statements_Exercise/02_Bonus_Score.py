number = int(input())
bonus_points = 0

if number <= 100:
    bonus_points = 5
elif 1000 >= number > 100:
    bonus_points = number * 0.20
elif number > 1000:
    bonus_points = number * 0.10

extra_bonus_points = 0

if number % 2 == 0:  # проверка за четност !
    extra_bonus_points = 1
elif number % 10 == 5:
    extra_bonus_points = 2

bonus_points = bonus_points + extra_bonus_points

print(bonus_points)
print(bonus_points + number)