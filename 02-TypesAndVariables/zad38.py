phone_number = input("Enter phone number: ")

if phone_number.isdigit() and len(phone_number) == 9:
    formatted_phone_number = f"{phone_number[:3]}-{phone_number[3:6]}-{phone_number[6:]}"
    print(f"Phone number: {formatted_phone_number}")
else:
    print("Invalid input. Please enter a 9-digit phone number.")
