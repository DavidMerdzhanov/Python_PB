

number = input()
total = 0

while number != "NoMoreMoney":
    current_number = float(number)
    if current_number < 0:
        print("Invalid operation!")
        break

    print(f"Increase: {current_number:.2f}")
    total += current_number
    number = input()

print(f"Total: {total:.2f}")



