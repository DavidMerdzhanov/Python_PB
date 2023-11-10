PUZZLE_PRICE = 2.60
DOLL_PRICE = 3
BEAR_PRICE = 4.10
MINION_PRICE = 8.20
TRUCK_PRICE = 2

price_for_hike = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())


money_earned = (PUZZLE_PRICE * number_of_puzzles) + \
               (DOLL_PRICE * number_of_dolls) + \
               (BEAR_PRICE * number_of_bears) \
               + (MINION_PRICE * number_of_minions) + \
               (TRUCK_PRICE * number_of_trucks)

total_toys_count = number_of_puzzles + number_of_dolls + number_of_bears + number_of_minions + number_of_trucks
if total_toys_count >= 50:
    money_earned = money_earned * (1 - 0.25)

money_earned = money_earned * (1 - 0.1)

if money_earned >= price_for_hike:

    print(f"Yes! {money_earned - price_for_hike:.2f} lv left.")
else:
    print(f"Not enough money! {price_for_hike - money_earned:.2f} lv needed.")
