# Subroutines, and specifically functions, are a convenient way to divide a program code into useful blocks, allowing to make a program code more readable, reuse it and save some time. A function is a block of code which only runs when it is called. There are a number of built-in functions, ready to use, e.g. len(), print(), input() or type().

# Using built-in Python functions, write a program that calculates and displays:

# a. length of the phrase: "computer science"
lenght = len("computer science")
print(lenght)


# b. letter read from the keyboard
letter = input("Enter the letter: ")
if len(letter) == 1 and letter.isdigit() == False:
    print(letter)
else:
    print("Invalid input. Try again")


# c. string representing the number 5068
number = 5068
number = str(number)
print(number)


# d. numeric representing the string "20303"
string = "20303"
string = int(string)
print(string)


# e. the smallest number given: 4,7,2,3,9,8
numbers = [4,7,2,3,9,8]
print(min(numbers))
