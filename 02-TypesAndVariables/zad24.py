registration_number = input("Enter vehicle registration number: ")

is_from_krakow = registration_number.startswith("KR") or registration_number.startswith("KK") or registration_number.startswith("kk") or registration_number.startswith("kr")

print(f"Car from Kraków: {is_from_krakow}")