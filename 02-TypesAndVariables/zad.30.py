import random 

roll = random.randint(1, 6)

is_sepcial = roll == 1 or roll == 6

print(f"Dice rolled: {roll}")
print(f"Special number: {is_sepcial}")

