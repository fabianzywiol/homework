def numbers(n):
    result = ""
    for i in range(1, n + 1):
        result += str(i) + " "
    return result

x = numbers(15)
y = numbers(7)

print(f'Numbers <1,15>: {x}')
print(f'Numbers <1,7>: {y}')
