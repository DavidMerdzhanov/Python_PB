
hours = int(input())
minutes = int(input())


extra_minutes = 15 + minutes

if extra_minutes >= 60:
    extra_minutes -= 60
    hours += 1

if hours >= 24:
    hours = 0

print(f"{hours}:{extra_minutes:02d}")




