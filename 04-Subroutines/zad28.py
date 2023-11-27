def f(amount_to_pay):
    coins = [5, 2, 1]
    total_coins = 0

    for coin in coins:
        total_coins += amount_to_pay // coin
        amount_to_pay %= coin

    return total_coins

print(f(23))  
print(f(8))   
print(f(2))   
print(f(0))   
    