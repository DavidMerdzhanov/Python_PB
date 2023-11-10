
target_amount = float(input())


coins_count = 0
target_amount_pennies = int(target_amount * 100)

while target_amount_pennies > 0:
    if target_amount_pennies >= 200:
        target_amount_pennies -= 200
        coins_count += 1
    elif target_amount_pennies >= 100:
        target_amount_pennies -= 100
        coins_count += 1
    elif target_amount_pennies >= 50:
        target_amount_pennies -= 50
        coins_count += 1
    elif target_amount_pennies >= 20:
        target_amount_pennies -= 20
        coins_count += 1
    elif target_amount_pennies >= 10:
        target_amount_pennies -= 10
        coins_count += 1
    elif target_amount_pennies >= 5:
        target_amount_pennies -= 5
        coins_count += 1
    elif target_amount_pennies >= 2:
        target_amount_pennies -= 2
        coins_count += 1
    elif target_amount_pennies >= 1:
        target_amount_pennies -= 1
        coins_count += 1


print(coins_count)

