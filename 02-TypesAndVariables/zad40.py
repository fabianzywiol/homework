credit_number = (input("Enter credit card number: "))

separated_credit_number = f"{credit_number[0:5]} {credit_number[4:9]} {credit_number[8:13]} {credit_number[12:17]}"

print(f"Card number: {separated_credit_number}")