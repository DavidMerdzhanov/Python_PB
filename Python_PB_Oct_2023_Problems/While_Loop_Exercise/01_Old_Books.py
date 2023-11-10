book_goal = input()
book_count = 0
is_found = False

command = input()
while command != "No More Books":

    if command == book_goal:
        is_found = True
        break

    book_count += 1
    command = input()


if not is_found:
    print(f"The book you search is not here!")
    print(f"You checked {book_count} books.")
else:
    print(f"You checked {book_count} books and found it.")
