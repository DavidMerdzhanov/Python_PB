

numbers = int(input())

p1_number = 0
p2_number = 0
p3_number = 0
p4_number = 0
p5_number = 0

for i in range(numbers):
    current_number = int(input())

    if current_number < 200:
        p1_number += 1
    elif current_number < 400:
        p2_number += 1
    elif current_number < 600:
        p3_number += 1
    elif current_number < 800:
        p4_number += 1
    else:
        p5_number += 1


p1_number_percentage = p1_number / numbers * 100
p2_number_percentage = p2_number / numbers * 100
p3_number_percentage = p3_number / numbers * 100
p4_number_percentage = p4_number / numbers * 100
p5_number_percentage = p5_number / numbers * 100

print(f"{p1_number_percentage: .2f}%")
print(f"{p2_number_percentage: .2f}%")
print(f"{p3_number_percentage: .2f}%")
print(f"{p4_number_percentage: .2f}%")
print(f"{p5_number_percentage: .2f}%")
