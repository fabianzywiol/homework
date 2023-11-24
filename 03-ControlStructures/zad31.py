x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))


if x == 0 and y == 0:
    print("The point ({x}, {y}) is located in the position (0,0)!")
elif x > 0 and y > 0:
    print("The point ({x}, {y}) is located in the first quadrant of the coordinate system!")
elif x < 0 and y > 0:
    print("The point ({x}, {y}) is located in the second quadrant of the coordinate system!")
elif x < 0 and y < 0:
    print("The point ({x}, {y}) is located in the third quadrant of the coordinate system!")
elif x > 0 and y < 0:
    print("The point ({x}, {y}) is located in the fourth quadrant of the coordinate system!")