total_days = 0
consecutive_spending = 0
is_failed = False


vacation_amount_money = float(input())
money_available = float(input())

total_money = money_available

while True:
    action = input()
    action_money = float(input())

    total_days += 1

    if action == "spend":
        consecutive_spending += 1
        if consecutive_spending >= 5:
            is_failed = True
            break

        total_money -= action_money
        if total_money <= 0:
            total_money = 0

    elif action == "save":
        consecutive_spending = 0
        total_money += action_money

        if total_money >= vacation_amount_money:
            break


if not is_failed:
    print(f"You saved the money for {total_days} days.")
else:
    print("You can't save the money.")
    print(total_days)



