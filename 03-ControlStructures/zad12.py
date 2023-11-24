first_name = str(input("Enter first person name: "))
first_age = int(input("Enter first person age: "))
second_name = str(input("Enter second persson name: "))
second_age = int(input("Enter second person age: "))

if first_age >= 18 and second_age >= 18:
    print(f"Both {first_name} and {second_name} are adults")
elif first_age < 18 and second_age >= 18:
    print(f"Only {second_name} is an adult")
elif first_age >= 18 and second_age < 18:
    print(f"Only {first_name} is an adult")
else:
    print(f"Both {first_name} and {second_name} are not adults ")