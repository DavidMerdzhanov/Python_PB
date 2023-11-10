

month = input()
number_of_nights = int(input())

studio = 0
apartment = 0

if month == "May" or month == "October":
    studio = 50
    apartment = 65
    if 7 < number_of_nights <= 14:
        studio *= (1 - 0.05)
    elif number_of_nights > 14:
        studio *= (1 - 0.3)


elif month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
    if number_of_nights > 14:
        studio *= (1 - 0.2)

elif month == "July" or month == "August":
    studio = 76
    apartment = 77

if number_of_nights > 14:
    apartment *= (1 - 0.1)

studio_total_cost = number_of_nights * studio
apartment_total_cost = number_of_nights * apartment

print(f"Apartment: {apartment_total_cost:.2f} lv.")
print(f"Studio: {studio_total_cost:.2f} lv.")