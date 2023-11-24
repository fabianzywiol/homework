current_price = float(input("Enter the current product price: "))
previous_price = float(input("Enter the previous product price: "))

percentage_decrease = ((previous_price - current_price) / previous_price) * 100

print(f"Current product price: {current_price:.2f}")
print(f"Previous product price: {previous_price:.2f}")

if percentage_decrease >= 10:
    print(f"Buy the product!!\nProduct price reduced by {percentage_decrease:.2f}%")
else:
    print("No need to buy the product. Price reduction is less than 10%.")
