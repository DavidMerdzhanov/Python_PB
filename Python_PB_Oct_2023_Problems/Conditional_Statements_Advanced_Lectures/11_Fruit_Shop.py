

fruit = input()
day_of_the_week = input()
amount = float(input())
price_for_fruit = 0
if day_of_the_week == "Monday" \
        or day_of_the_week == "Tuesday" \
        or day_of_the_week == "Wednesday" \
        or day_of_the_week == "Thursday" \
        or day_of_the_week == "Friday":
    if fruit == "banana":
        price_for_fruit = 2.50

    elif fruit == "apple":
        price_for_fruit = 1.20

    elif fruit == "orange":
        price_for_fruit = 0.85

    elif fruit == "grapefruit":
        price_for_fruit = 1.45

    elif fruit == "kiwi":
        price_for_fruit = 2.70

    elif fruit == "pineapple":
        price_for_fruit = 5.50

    elif fruit == "grapes":
        price_for_fruit = 3.85


elif day_of_the_week == "Saturday" or day_of_the_week == "Sunday":
    if fruit == "banana":
        price_for_fruit = 2.70

    elif fruit == "apple":
        price_for_fruit = 1.25

    elif fruit == "orange":
        price_for_fruit = 0.90

    elif fruit == "grapefruit":
        price_for_fruit = 1.60

    elif fruit == "kiwi":
        price_for_fruit = 3.00

    elif fruit == "pineapple":
        price_for_fruit = 5.60

    elif fruit == "grapes":
        price_for_fruit = 4.20

if price_for_fruit == 0:
    print("error")
else:
    price_for_fruit *= amount
    print(f"{price_for_fruit:.2f}")











