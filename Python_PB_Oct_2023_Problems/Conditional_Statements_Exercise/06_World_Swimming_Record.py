import math

world_record_sec = float(input())
distance_in_meters = float(input())
time_in_seconds_meter = float(input())


all_time_in_seconds_of_ivan = distance_in_meters * time_in_seconds_meter
slow_water_resistance = math.floor(distance_in_meters / 15) * 12.5
total_time = all_time_in_seconds_of_ivan + slow_water_resistance

if world_record_sec <= total_time:
    print(f"No, he failed! He was {total_time - world_record_sec:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")

