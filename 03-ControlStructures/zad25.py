purchased_products = int(input("Number of products purchased: "))

product_price = float(input("Product price: "))

if purchased_products > 2:
    total_amount = purchased_products * product_price

    discount_amount = (purchased_products - 2) * 0.25 * product_price

    final_amount = total_amount - discount_amount

    print(f"Kwota do zapłaty: {final_amount:.2f}")
else:
    final_amount = purchased_products * product_price
    print(f"Kwota do zapłaty: {final_amount:.2f}")

