

mackerel_price_per_kilo = float(input())
sprinkle_price_per_kilo = float(input())
kilos_of_bonito = float(input())
kilogram_of_saffron = float(input())
kilo_of_mussels = int(input())


bonito_price = mackerel_price_per_kilo * 1.6
sum_bonito = kilos_of_bonito * bonito_price
saffron_price = sprinkle_price_per_kilo * 1.8
sum_saffron = kilogram_of_saffron * saffron_price
mussels = kilo_of_mussels * 7.50

total_cost = sum_bonito + sum_saffron + mussels

print(f"{total_cost:.2f}")