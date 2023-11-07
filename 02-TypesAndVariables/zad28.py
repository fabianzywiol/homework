height_cm = float(input("Enter your height in cm: "))
weight_kg = float(input("Enter your weight in kg: "))

height_m = height_cm / 100

bmi = weight_kg / (height_m ** 2)

is_weight_correct = 18.5 <= bmi <= 24.9

print(f"Your bmi index: {bmi}")
print(f"Correct weight: {is_weight_correct}")