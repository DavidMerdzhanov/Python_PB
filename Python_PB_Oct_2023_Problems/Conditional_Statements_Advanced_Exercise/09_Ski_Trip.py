

days_to_stay = int(input())
type_of_residence = input()
rating_of_Atanas = input()


price_for_residence = 0
discount = 0

if type_of_residence == "room for one person":
    price_for_residence = 18

if type_of_residence == "apartment":
    price_for_residence = 25
    if days_to_stay < 10:
        discount = 0.3
    elif 10 <= days_to_stay <= 15:
        discount = 0.35
    else:
        discount = 0.5


elif type_of_residence == "president apartment":
    price_for_residence = 35
    if days_to_stay < 10:
        discount = 0.1
    elif 10 <= days_to_stay <= 15:
        discount = 0.15
    else:
        discount = 0.2


total_price_in_hotel = (days_to_stay - 1) * price_for_residence * (1 - discount)

if rating_of_Atanas == "positive":
    total_price_in_hotel += (total_price_in_hotel * 0.25)   # total_price_in_hotel *= 1.25
elif rating_of_Atanas == "negative":
    total_price_in_hotel -= (total_price_in_hotel * 0.1)    # total_price_in_hotel *= 0.9

print(f"{total_price_in_hotel:.2f}")















