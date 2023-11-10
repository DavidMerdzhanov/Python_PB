destination = input()
while destination != "End":
    budged = float(input())
    current_money = 0
    while current_money < budged:
        saved_money = float(input())
        current_money += saved_money

    print(f"Going to {destination}!")
    destination = input()
