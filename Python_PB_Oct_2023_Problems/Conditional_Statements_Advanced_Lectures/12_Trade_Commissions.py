

name_of_city = input()

amount_of_sales = float(input())

commission = 0

if name_of_city == "Sofia":
    if 0 <= amount_of_sales <= 500:
        commission = (amount_of_sales * 0.05)

    elif 500 < amount_of_sales <= 1_000:
        commission = (amount_of_sales * 0.07)

    elif 1_000 < amount_of_sales <= 10_000:
        commission = (amount_of_sales * 0.08)

    elif amount_of_sales > 10_000:
        commission = (amount_of_sales * 0.12)

if name_of_city == "Varna":
    if 0 <= amount_of_sales <= 500:
        commission = (amount_of_sales * 0.045)

    elif 500 < amount_of_sales <= 1_000:
        commission = (amount_of_sales * 0.075)

    elif 1_000 < amount_of_sales <= 10_000:
        commission = (amount_of_sales * 0.1)

    elif amount_of_sales > 10_000:
        commission = (amount_of_sales * 0.13)


if name_of_city == "Plovdiv":
    if 0 <= amount_of_sales <= 500:
        commission = (amount_of_sales * 0.055)

    elif 500 < amount_of_sales <= 1_000:
        commission = (amount_of_sales * 0.08)

    elif 1_000 < amount_of_sales <= 10_000:
        commission = (amount_of_sales * 0.12)

    elif amount_of_sales > 10_000:
        commission = (amount_of_sales * 0.145)

if amount_of_sales < 0 or commission == 0:
    print("error")
else:
    print(f"{commission:.2f}")













