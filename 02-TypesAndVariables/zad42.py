binary_input = input("Enter binary number: ")

if len(binary_input) == 4 and binary_input.isnumeric() and all(bit in '01' for bit in binary_input):
    decimal_result = 0
    for i in range(4):
        decimal_result += int(binary_input[i]) * 2**(3 - i)
    print(f"Binary number in decimal notation: {decimal_result}")
else:
    print("Invalid input. Please enter a 4-digit binary number.")
