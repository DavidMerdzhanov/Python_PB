

judges = int(input())

presentation_count = 0
total_score = 0

command = input()
while command != "Finish":
    presentation = command
    presentation_count += 1

    current_score = 0
    for i in range(judges):
        judges_score = float(input())
        current_score += judges_score

    average_score = current_score / judges
    print(f"{presentation} - {average_score:.2f}.")
    total_score += current_score

    command = input()

total_average_score = total_score / (presentation_count * judges)
print(f"Student's final assessment is {total_average_score:.2f}.")














