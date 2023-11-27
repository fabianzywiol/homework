def read_number():
    while True:
        user_input = input("Enter a number: ")
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    num1 = read_number()
    num2 = read_number()

    sum_result = num1 + num2
    print(f"{num1} + {num2} = {sum_result}")
