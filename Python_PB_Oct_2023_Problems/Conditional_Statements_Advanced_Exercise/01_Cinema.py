

screening_type = input()
number_of_rows = int(input())
number_of_columns = int(input())

income = 0
cinema_capacity = number_of_rows * number_of_columns

if screening_type == "Premiere":
    income = cinema_capacity * 12.00
elif screening_type == "Normal":
    income = cinema_capacity * 7.50
elif screening_type == "Discount":
    income = cinema_capacity * 5.00

print(f"{income:.2f} leva")
