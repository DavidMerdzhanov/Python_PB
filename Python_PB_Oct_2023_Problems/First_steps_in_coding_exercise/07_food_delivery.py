CHICKEN_MENU = 10.35
FISH_MENU = 12.40
VEGETARIAN_MENU = 8.15
price_for_delivery = 2.50


number_of_chicken_menu = int(input())
number_of_fish_menu = int(input())
number_of_vegetarian_menu = int(input())

total_cost_menu = (number_of_chicken_menu * CHICKEN_MENU) + (number_of_fish_menu * FISH_MENU) \
    + (number_of_vegetarian_menu * VEGETARIAN_MENU)

price_of_dessert = total_cost_menu * (1 - 0.80)

total_price_order = total_cost_menu + price_of_dessert + price_for_delivery
print(total_price_order)


