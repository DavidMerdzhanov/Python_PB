

budged = float(input())
number_of_video_cards = int(input())
number_of_cpu = int(input())
number_of_ram = int(input())

video_card_price = 250
discount_for_cpu = (number_of_video_cards * video_card_price) * 0.35
cpu_price = number_of_cpu * discount_for_cpu

discount_for_ram = (number_of_video_cards * video_card_price) * 0.10
ram_price = number_of_ram * discount_for_ram

needed_amount = (number_of_video_cards * video_card_price) + (cpu_price + ram_price)

if number_of_video_cards > number_of_cpu:
    needed_amount = needed_amount * 0.85

if budged >= needed_amount:
    print(f"You have {budged - needed_amount:.2f} leva left!")
else:
    print(f"Not enough money! You need {needed_amount - budged:.2f} leva more!")




