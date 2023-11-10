

text = input()

value = 0

for chart in text:
    if chart == "a":
        value += 1
    elif chart == "e":
        value += 2
    elif chart == "i":
        value += 3
    elif chart == "o":
        value += 4
    elif chart == "u":
        value += 5

print(value)