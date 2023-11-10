number_of_groups = int(input())

MUSALA_climbers = 0
MONBLAN_climbers = 0
KILIMANJARO_climbers = 0
K2_climbers = 0
EVEREST_climbers = 0


total_count = 0

for i in range(number_of_groups):
    number_of_people_in_group = int(input())
    total_count += number_of_people_in_group

    if number_of_people_in_group <= 5:
        MUSALA_climbers += number_of_people_in_group

    elif number_of_people_in_group <= 12:
        MONBLAN_climbers += number_of_people_in_group

    elif number_of_people_in_group <= 25:
        KILIMANJARO_climbers += number_of_people_in_group

    elif number_of_people_in_group <= 40:
        K2_climbers += number_of_people_in_group

    else:
        EVEREST_climbers += number_of_people_in_group


percentage_MUSALA_climbers = MUSALA_climbers / total_count * 100
percentage_MONBLAN_climbers = MONBLAN_climbers / total_count * 100
percentage_KILIMANJARO_climbers = KILIMANJARO_climbers / total_count * 100
percentage_K2_climbers = K2_climbers / total_count * 100
percentage_EVEREST_climbers = EVEREST_climbers / total_count * 100

print(f"{percentage_MUSALA_climbers:.2f}%")
print(f"{percentage_MONBLAN_climbers:.2f}%")
print(f"{percentage_KILIMANJARO_climbers:.2f}%")
print(f"{percentage_K2_climbers:.2f}%")
print(f"{percentage_EVEREST_climbers:.2f}%")

