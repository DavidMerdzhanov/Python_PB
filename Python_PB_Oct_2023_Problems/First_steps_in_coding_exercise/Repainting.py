nylon_price = 1.50
paint_price = 14.50  # for liter
paint_thinner_price = 5.00  # for liter
bag_price = 0.40

amount_nylon = int(input())
amount_paint = int(input())
amount_paint_thinner = int(input())
hours_of_work = int(input())

nylon_extra_added = 2
paint_extra_added = amount_paint * 0.10

total_material_price = (amount_nylon + nylon_extra_added) * nylon_price \
    + (amount_paint + paint_extra_added) * paint_price \
    + (amount_paint_thinner * paint_thinner_price) + bag_price
work_per_hours_price = (total_material_price * 0.30) * 8
final_amount = work_per_hours_price + total_material_price
print(final_amount)












