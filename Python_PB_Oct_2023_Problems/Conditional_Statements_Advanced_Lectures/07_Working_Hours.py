

hour_from_day = int(input())
day_of_the_week = input()

if 10 <= hour_from_day <= 18:
    if day_of_the_week == "Monday" \
            or day_of_the_week == "Tuesday" \
            or day_of_the_week == "Wednesday" \
            or day_of_the_week == "Thursday" \
            or day_of_the_week == "Friday" \
            or day_of_the_week == "Saturday":
        print("open")


if hour_from_day > 18 or hour_from_day < 10 or day_of_the_week == "Sunday":
    print("closed")



