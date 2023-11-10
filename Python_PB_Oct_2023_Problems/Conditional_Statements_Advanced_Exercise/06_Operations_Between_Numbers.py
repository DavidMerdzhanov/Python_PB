

n1 = int(input())
n2 = int(input())
operator_symbol = input()

if operator_symbol == "+":
    result = n1 + n2
    even_or_odd = ""
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{n1} {operator_symbol} {n2} = {result} - {even_or_odd}")

elif operator_symbol == "-":
    result = n1 - n2
    even_or_odd = ""
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{n1} {operator_symbol} {n2} = {result} - {even_or_odd}")

elif operator_symbol == "*":
    result = n1 * n2
    even_or_odd = ""
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{n1} {operator_symbol} {n2} = {result} - {even_or_odd}")


if operator_symbol == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero ")
    else:
        result = n1 / n2
        print(f"{n1} / {n2} = {result:.2f}")


if operator_symbol == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero ")
    else:
        result = n1 % n2
        print(f"{n1} % {n2} = {result}")



