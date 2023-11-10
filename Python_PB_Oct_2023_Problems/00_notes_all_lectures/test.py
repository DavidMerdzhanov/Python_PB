#
# for attempt in range(1, 6):  # [1, 2, 3, 4, 5]
#     print(f"Attempt No {attempt}")
#     print("Trying to connect to DB...")
#     if attempt == 3:
#         print("Success!!!")
#         break
#

# text = "I am feeling good"
#
# print(len(text))  # 17
#
# print(text[2])  # "a"


#
#
# for i in range(10):       # [0, 1, 2..., 9]
#     if 3 <= i < 5:
#         print('between 3 & 5')
#         continue
#
#     print('core logic here line 1')
#     print('core logic here line 2')



#
# is_break = False
# for i in range(15):
#     print(i)
#     if i == 10:
#         print('exit with break')
#         is_break = True
#         break
#

# number = int(input())
#
# if number > 100:
#     print('more than 100')
# elif number > 10:
#     print('more than 10')
# else:
#     print('something else')


#
# my_name = "Simo"  # = input()
#
# print(my_name[0])
# print(my_name[1])
# print(my_name[2])
# print(my_name[3])
# print('------')
# print("abcdef"[2])
#
# print("Sept" == "Sept ")





# for number in range(1, 25, 3):  # [2, 3]  == [2; 4)
#     print(number)
#     # print(type(number))
#     # print('we are here!')
#
# print('---')
# print('after the for-cycle')

# num = int(input())
#
# if num > 10:
#     my_var = 1337
# else:
#     my_var = 100
#
# print(my_var)

# PyCharm -> IDE

# help(range)
# range()

# text = "I am feeling good"
#
# print(len(text))  # 17
#
# print(text[2])  # "a"

# for attempt in range(1, 6):  # [1, 2, 3, 4, 5]
#     print(f"Attempt No {attempt}")
#     print("Trying to connect to DB...")
#     if attempt == 3:
#         print("Success!!!")
#         break

# print("final value")
# print(attempt)
# for _ in range(5):  # [0, 1, 2, 3, 4]
#     print("Trying to connect to DB...")

# for i in range(1, 25, 3):
#     print(i)
#     if i == 10:
#         print('here')
#         continue
#
#     print("after IF, but inside FOR")

# for i in range(10):  # [0, 1, 2..., 9]
#     if 3 <= i < 5:
#         print('between 3 & 5')
#         continue
#
#     print('core logic here line 1')
#     print('core logic here line 2')

# number = 2 / 3  # 0.6666666666666666666666666
#
# print(f"{number :.2%}")

# is_break = False
# for i in range(15):
#     print(i)
#     if i == 10:
#         print('exit with break')
#         is_break = True
#         break
# else:
#     print("WAS ENDED WITHOUT BREAK")
#
# if is_break:
#     print("was broken")
# else:
#     print("was NOT broker")
# ...

# number = int(input())
#
# if number > 100:
#     print('more than 100')
# elif number > 10:
#     print('more than 10')
# else:
#     print('something else')
# import math
# import sys
#
# number = 13.333337
#
# print(math.ceil(number))
# print(math.floor(number))

# help(sys.maxsize)

# my_name = "Simo"  # = input()
#
# print(my_name[0])
# print(my_name[1])
# print(my_name[2])
# print(my_name[3])
# print('------')
# print("abcdef"[2])

# print("Sept" == "Sept ")

# text = "Hello Bulgaria!😍"
#
# # for i in range(len(text)):
# #     print(f"index {i}: character: {text[i]}")
#
# for idx, char in enumerate(text):
#     print(f"index {idx}: char: {char}")











# print('yes, it works')

# for attempt in range(1, 6):  # [1, 2, 3, 4, 5]
#     print(f"Attempt No {attempt}")
#     print("Trying to connect to DB...")


# while not is_connected:
#     try_to_connect

# number = 13
#
# while number < 200:
#     print(f"Current number {number}")
#
#     number += 10

# number = 1337
# while number <= 2000:
#     print('less than 2000')
#
#     if number % 2 == 0:
#         break
#
#     print('will never be printed')
#
#
#     number += 13

# name = input()
# age = int(input())
#
# if name == "Simo" and age == 13:
#     print(f"Average score: 5.60\nNumber of problems: 5\nLast problem: IronMan")
# elif name == "Vanko" and age == 15:
#     print(f"You need a break, 2 poor grades.")

# num1 = 0.1 + 0.2
# num2 = 0.3
#
# print(num1 == num2)
# print(num1)

# operators -> break AND continue

# name = input()
#
# while name != "Simo":
#     print(f"Hello, {name}")
#
#     if name == "XXX":
#         name = input()
#         continue
#
#     print(f"You are not Simo OR XXX")
#
#     name = input()













# budget = 0
# while budget < 1000:  # vacation_cost = 1000
#     print('I am saving 150...')
#     budget += 150
#
# print(f"Yes, I am going to vacation with 1000 cost, because I saved {budget}")

# money_needed = 1000
# should_break = False
# budget = 0
# for day in range(1, 6):   # [1, 2, 3, 4, 5]
#     print(f"=> I am working day - {day}")
#     for hour in range(1, 9):  # [1, 2, 3, 4, 5, 6, 7, 8]
#         if hour == 5:
#             print(f"Hour {hour} - I am taking a break")
#             continue
#         print(f"--- I am working hour - {hour}; still day is {day}")
#         budget += 150
#
#         if budget >= 1000:
#             should_break = True
#             break
#
#     if should_break:
#         break
#
# print('---')
# print(budget)

# print('line 1')
# print()  # print('') end='\n'
# print('line 2')

# my_name = 'Simo'
# print(my_name[0])
# print(my_name[1])
# print(my_name[2])

# int("stop")

# number = int(input())
#
# is_prime = True
# for n in range(2, number):  # [2, 3, ..., number - 1]
#     if number % n == 0:  # 3 % 1 == 0; 3 % 3 == 0
#         is_prime = False
#         break
#
#
# if is_prime:
#     print(f"{number} is prime")
# else:
#     print(f"{number} is not prime")
# number = 1
#
# for num in range(2, number):  # range(2, 1) => []
#     print('here')
#     print(num)

# number = 10
# 10 % 2 == 0 -> is_prime = False
# 10 % 3 == 0
# 10 % 4 == 0
# 10 % 5 == 0

# for n in range(1_111, 9_999):
#     # check if n is_special
#     # if special -> print
#     print(f"{n} ", end="")

# num = int(input())
#
# num_as_string = str(num)

#
# for _, digit in enumerate("4911"):
#     # print(f"idx hold {idx}; digit hold {digit}")
#     print(f"digit - {digit}")  # "4", "9"
#     print(type(digit))
#
# # print(3 // 0)

# for num in range(10):dsdsdsdsds
#     print(num)

# for digit in "4123":
#     print(digit)
# n = 3
# is_special = True
# for _, digit in enumerate("1100"):  # n -> 1_111, ..., 9_999
#     digit_as_int = int(digit)  # int("1") == 1
#
#     if digit_as_int == 0:
#         continue
#
#     if n % digit_as_int != 0:
#         is_special = False
#         break
#
# if is_special:
#     print(f"{n} ", end="")


# print(ord("a"))
# print(ord("A"))
# print(ord("b"))
# print(ord("c"))
# ASCII

# print(chr(97))
# print(chr(65))
# print(chr(98))
# print(chr(99))


















