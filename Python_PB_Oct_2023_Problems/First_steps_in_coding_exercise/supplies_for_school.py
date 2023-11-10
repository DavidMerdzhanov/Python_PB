
PACK_OF_PENS = 5.80
PACK_OF_MARKERS = 7.20
PREPARATION = 1.20  # For liter

number_of_pens = int(input())
number_of_markers = int(input())
liters_of_clean_preparation = int(input())
discount = int(input())
price_of_pack_of_pens = number_of_pens * PACK_OF_PENS
price_of_pack_of_markers = number_of_markers * PACK_OF_MARKERS
price_of_preparation = liters_of_clean_preparation * PREPARATION
price_of_all_products = price_of_pack_of_pens + price_of_pack_of_markers + price_of_preparation
discount_price = price_of_all_products - (price_of_all_products * 0.25)
print(discount_price)




