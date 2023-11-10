

budget = int(input())
season = input()
num_fisherman = int(input())


price_for_the_ship = 0
discount = 0

if season == "Spring":
    price_for_the_ship = 3000

elif season == "Summer" or season == "Autumn":
    price_for_the_ship = 4200

elif season == "Winter":
    price_for_the_ship = 2600

if num_fisherman <= 6:
    discount = 0.1

elif 7 <= num_fisherman <= 11:
    discount = 0.15

elif num_fisherman >= 12:
    discount = 0.25

total_cost = price_for_the_ship * (1 - discount)

if not season == "Autumn":
    if num_fisherman % 2 == 0:
        total_cost *= (1 - 0.05)


if budget >= total_cost:
    print(f"Yes! You have {budget - total_cost:.2f} leva left.")
else:
    print(f"Not enough money! You need {total_cost - budget:.2f} leva.")