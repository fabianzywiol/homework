bought_euro = float(input("Bank buys EUR: "))

sold_euro = float(input("Bank sells EUR: "))

spread = bought_euro - sold_euro

converted_spread = "{:.4f}".format(spread)

print(f"Spread: {converted_spread}")