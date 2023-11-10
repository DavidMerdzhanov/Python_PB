

budget_film = float(input())
number_of_statists = int(input())
clothing_price_for_one_statist = float(input())


decor_for_film = budget_film * 0.10

if number_of_statists > 150:
    clothing_price_for_one_statist *= (1 - 0.10)

mooney_needed = decor_for_film + number_of_statists * clothing_price_for_one_statist


budget_enough = f"Action!\nWingard starts filming with {budget_film - mooney_needed:.2f} leva left."
budget_not_enough = f"Not enough money!\nWingard needs {mooney_needed- budget_film:.2f} leva more."

if mooney_needed > budget_film:
    print(budget_not_enough)
else:
    print(budget_enough)
