

# •	"Facebook" -> 150 лв.
# •	"Instagram" -> 100 лв.
# •	"Reddit" -> 50 лв.

tab_opened = int(input())
salary = int(input())

is_salary = True

for i in range(tab_opened):
    name_of_browser = input()

    if name_of_browser == "Facebook":
        salary -= 150
    elif name_of_browser == "Instagram":
        salary -= 100
    elif name_of_browser == "Reddit":
        salary -= 50

    if salary <= 0:
        is_salary = False
        break

if is_salary:
    print(int(salary))
else:
    print("You have lost your salary.")

