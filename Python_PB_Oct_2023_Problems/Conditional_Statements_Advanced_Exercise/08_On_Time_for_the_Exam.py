
exam_hour = int(input())  # 0 - 23
exam_minute = int(input())  # 0 - 59
arrival_hour = int(input())  # 0 - 23
arrival_minute = int(input())  # 0 - 59

exam_time = exam_hour * 60 + exam_minute
arrival_time = arrival_hour * 60 + arrival_minute

difference = exam_time - arrival_time

if difference < 0:
    print("Late")

elif 0 <= difference <= 30:
    print("On time")
else:
    print("Early")

if difference != 0:
    hour = abs(difference) // 60
    minute = abs(difference) % 60

    if difference < 0:
        if hour > 0:
            print(f"{hour}:{minute:02d} hours after the start")
        else:
            print(f"{minute} minutes after the start")
    else:
        if hour > 0:
            print(f"{hour}:{minute:02d} hours before the start")
        else:
            print(f"{minute} minutes before the start")







#
# x = abs(20) % 60
# print(x)
#




