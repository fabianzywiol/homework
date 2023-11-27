import mymath
import mykeyboard


def main():
    user_number = mykeyboard.read_number()
    computer_number = mymath.generate_number()

    print(f"Computer number: {computer_number}")

    if user_number == computer_number:
        print("You won the game!!")
    else:
        print("Try again. You didn't win this time.")

if __name__ =="__main__":
    main()