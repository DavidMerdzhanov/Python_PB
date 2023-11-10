budget = float(input())
seasons = input()

destination = ""
rest = ""
percent_from_budget = 0

if budget <= 100:
    destination = "Bulgaria"
    if seasons == "summer":
        percent_from_budget = 0.3
        rest = "Camp"

    elif seasons == "winter":
        percent_from_budget = 0.7
        rest = "Hotel"

if 100 < budget <= 1000:
    destination = "Balkans"
    if seasons == "summer":
        percent_from_budget = 0.4
        rest = "Camp"

    elif seasons == "winter":
        percent_from_budget = 0.8
        rest = "Hotel"

if budget > 1000:
    destination = "Europe"
    if seasons == "summer" or seasons == "winter":
        percent_from_budget = 0.9
        rest = "Hotel"

total_cost = budget * percent_from_budget

print(f"Somewhere in {destination}")
print(f"{rest} - {total_cost:.2f}")
