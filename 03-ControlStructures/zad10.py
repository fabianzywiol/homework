number = int(input("Enter your number: "))

if number > 0:
    print(f"Absolute value of your number: {number}")
elif number < 0:
    number2 = number * (-1)
    print(f"Absolute value of your number: {number2}")
else:
    print(f"Absolute value of your number: 0")