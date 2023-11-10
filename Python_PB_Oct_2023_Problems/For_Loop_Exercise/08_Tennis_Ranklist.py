import math

number_of_tournaments = int(input())
starting_point_in_rank_list = int(input())


points = 0
win_points = 0
for i in range(number_of_tournaments ):
    stage_of_the_tournament = input()
    if stage_of_the_tournament == "W":
        points += 2000
        win_points += 1

    elif stage_of_the_tournament == "F":
        points += 1200

    elif stage_of_the_tournament == "SF":
        points += 720

points_of_all_tournaments = points + starting_point_in_rank_list
average_points_earned_per_tournament = points / number_of_tournaments
percentage_win_tournament = (win_points / number_of_tournaments) * 100

print(f"Final points: {points_of_all_tournaments}")
print(f"Average points: {math.floor(average_points_earned_per_tournament)}")
print(f"{percentage_win_tournament:.2f}%")