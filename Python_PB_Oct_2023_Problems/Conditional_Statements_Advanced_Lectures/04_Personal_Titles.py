

age = float(input())
gender = input()

if gender == "f" and age < 16:
    print("Miss")
elif gender == "m" and age >= 16:
    print("Mr.")
elif gender == "f" and age >= 16:
    print("Ms.")
else:
    if gender == "m" and age < 16:
        print("Master")


