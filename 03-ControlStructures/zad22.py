name = str(input(f"Enter name: "))

if name.lower().endswith('a'):
    print(f"{name} is likely a female name.")
else:
    print(f"{name} may not be a female name.")
