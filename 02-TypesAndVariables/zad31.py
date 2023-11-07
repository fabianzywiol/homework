import random 

print("Challenge the computer!")

roll = random.randint(1, 6)

guess = int(input(f"Guess the rolled number: "))

is_correct = roll == guess

print(f"Have you guessed?: {is_correct}!")
print(f"The dice rolled number was: {roll}")
