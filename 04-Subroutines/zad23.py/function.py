def is_within_range(x, y):
    entered_number = int(input("Enter a number: "))
    if entered_number >= x and entered_number <= y:
        print(f"Number {entered_number} is in range <{x}, {y}>: yes")
    else:
        print(f"Number {entered_number} is in range <{x}, {y}>: no")
