# / 1л=1 дм3/.

length = int(input())
width = int(input())
height = int(input())
percent_not_empty = float(input()) / 100   # 17 input means ---> 0.17 == 17%

fish_tank_volume_in_centimeters = length * width * height  # sm3
fish_tank_volume_in_liters = fish_tank_volume_in_centimeters / 1000  # 1l == 1dm3

water_needed_liters = fish_tank_volume_in_liters * (1 - percent_not_empty)
print(water_needed_liters)


