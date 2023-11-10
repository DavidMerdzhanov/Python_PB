N = int(input("Въведете цяло число N: "))

special_numbers = []

for num in range(1111, 10000):
    if all(N % int(digit) == 0
           if int(digit) != 0
           else
           False for digit in str(num)):
        special_numbers.append(num)

print(f"Специалните числа за N = {N} са: {special_numbers}")
