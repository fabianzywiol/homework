name = input("Enter your name: ")

print("Name:", end=" ")
for letter in name:
    print(f"{letter}({ord(letter)})", end=" ")

