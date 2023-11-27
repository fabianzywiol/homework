def count_negative_even_numbers(x, y):
    count = 0

    for number in range(x, y + 1):
        if number < 0 and number % 2 == 0:
            count += 1

    return count

print(count_negative_even_numbers(-7, 8))
print(count_negative_even_numbers(-1, 11)) 