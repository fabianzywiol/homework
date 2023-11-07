product_price = float(input("Enter price: "))
discount_percentage = float(input("Enter discount %: "))

discount = (discount_percentage / 100) * product_price
discounted_price = product_price - discount

price_difference = product_price - discounted_price

formatted_product_price = "{:.2f}".format(product_price)
formatted_discount = "{:.2f}".format(discount)
formatted_discounted_price = "{:.2f}".format(discounted_price)
formatted_price_difference = "{:.2f}".format(price_difference)

print(f"Price with discount: {formatted_discounted_price}")
print(f"Reduction: {formatted_price_difference}")

