points = float(input("Enter your points: "))
max_points = 100
test_passed = points >= 0.5 * (max_points)

if test_passed:
    print("Test passed!")
else:
    print("Test not passed")

