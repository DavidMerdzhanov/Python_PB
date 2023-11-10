
exchange_rate_euro = 1.94

price_for_vegetable_kg = float(input())
price_for_fruits_kg = float(input())
sum_kg_vegetable = int(input())
sum_kg_fruits = int(input())

vegetable_price = price_for_vegetable_kg * sum_kg_vegetable
fruits_price = price_for_fruits_kg * sum_kg_fruits
total_price = (vegetable_price + fruits_price) / exchange_rate_euro

print(f"{total_price:.2f}")