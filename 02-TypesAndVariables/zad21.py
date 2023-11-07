height_in_cm = float(input("Write your height in cm: "))

height_in_inches = height_in_cm / 2.54
height_in_feet = int(height_in_inches // 12)
remaining_inches = height_in_feet % 12

print(f"I am {height_in_cm} cm tall, i.e. {height_in_feet} feet and {height_in_inches} inches")