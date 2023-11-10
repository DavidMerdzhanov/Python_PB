import math

name_of_series = input()
duration_of_episode = int(input())
duration_of_break = int(input())


time_for_lunch = duration_of_break / 8
time_for_rest = duration_of_break / 4
time_left = (duration_of_break - time_for_lunch - time_for_rest)

if time_left >= duration_of_episode:
    print(f"You have enough time to watch \
{name_of_series} and left with {math.ceil(time_left) - duration_of_episode} minutes free time.")
else:
    print(f"You don't have enough time to watch \
{name_of_series}, you need {math.ceil(duration_of_episode) - math.floor(time_left)} more minutes.")
