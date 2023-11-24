question1 = str(input("Are you interested in computer science? (Y/N): ")).upper()
question2 = str(input("Do you like playing computer games? (Y/N): ")).upper()
question3 = str(input("Do you have an Instagram account (Y/N): ")).upper()

if question1 == "Y":
    print("Interested in computer science: Yes")
elif question1 ==  "N":
    print("Interested in computer science: No")
else: 
    print("Wrong format answer to question number 1. Try again.")

if question2 == "Y":
    print("Playing computer games: Yes")
elif question2 == "N":
    print("Playing computer games: No")
else:
    print("Wrong format answer to question number 2. Try again.")

if question3 == "Y":
    print("Has an instagram account: Yes")
elif question3 == "N":
    print("Has an Instagram account: No")
else: print("Wrong format answer to question number 32. Try again.")