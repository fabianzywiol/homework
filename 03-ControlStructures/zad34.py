amount = int(input("Enter your amount of money: "))

coins5 = 0
coins2 = 0
coins1 = 0

while amount >= 5:
    coins5 += 1
    amount -= 5

while amount >= 2:
    coins2 += 1
    amount -= 2

while amount >= 1:
    coins1 += 1
    amount -= 1

print(f"The amount of PLN {amount} in coins: \n 5 zł - {coins5} \n 2 zł - {coins2} \n 1 zł - {coins1}")


