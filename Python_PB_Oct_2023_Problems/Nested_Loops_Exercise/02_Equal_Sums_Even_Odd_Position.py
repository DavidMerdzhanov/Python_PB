

number_one = int(input())
number_two = int(input())


for number in range(number_one, number_two + 1):
    number_to_str = str(number)
    even_sum = 0
    odd_sum = 0
    for index, degit in enumerate(number_to_str):
        if index % 2 == 0:
            even_sum += int(degit)
        else:
            odd_sum += int(degit)

    if even_sum == odd_sum:
        print(number, end=" ")

