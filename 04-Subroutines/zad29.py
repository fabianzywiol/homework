def sum_of_digits(number, even):
    return sum(int(digit) for digit in str(number) if (int(digit) % 2 == 0) == even)

# Test cases
print(sum_of_digits(3124, True))     # Should return 6 (even digits: 2, 4)
print(sum_of_digits(3124, False))    # Should return 4 (odd digits: 3, 1)
print(sum_of_digits(20576, False))   # Should return 12 (odd digits: 5, 7)
print(sum_of_digits(20576, True))    # Should return 8 (even digits: 0, 6)
print(sum_of_digits(13115, True))    # Should return 0 (no even digits)

