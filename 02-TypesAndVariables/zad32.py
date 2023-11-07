amount = float(input("Enter the amount: "))

vat = amount * 0.23

formatted_amount = "{:.2f}".format(amount)
formatted_vat = "{:.2f}".format(vat)

print(f"Amount  : {formatted_amount}")
print(f"VAT 23% : {formatted_vat}")
