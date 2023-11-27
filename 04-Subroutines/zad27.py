def is_valid_binary(binary_number):
    for znak in binary_number:
        if znak != '0' and znak != '1':
            return False
    return True

print(is_valid_binary("101101")) 
print(is_valid_binary("1311a10100"))

