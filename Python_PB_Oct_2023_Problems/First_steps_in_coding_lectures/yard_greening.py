

PRICE_PER_SQUARE_METER = 7.61
square_meter = float(input())
price_for_whole_yard = square_meter * PRICE_PER_SQUARE_METER
discount = price_for_whole_yard * (1 - 0.82)
final_price = price_for_whole_yard - discount
print(f"The final price is {final_price} lv. ")
print(f"The discount is {discount} lv.")
