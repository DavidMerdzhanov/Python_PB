
name_of_actor = input()
points_from_academy = float(input())
number_of_evaluative = int(input())

total_points = points_from_academy

for i in range(number_of_evaluative):
    judge_name = input()
    judge_points = float(input())
    real_points = len(judge_name) * judge_points / 2
    total_points += real_points

    if total_points > 1250.5:
        break


if total_points <= 1250.5:
    print(f"Sorry, {name_of_actor} you need {1250.5 - total_points:.1f} more!")
else:
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {total_points:.1f}!")

