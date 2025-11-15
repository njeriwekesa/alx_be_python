# This code prints a square pattern of asterisks with the specified size.

size = int(input("Enter the size of the pattern: "))

row = 0
while row < size:
    for _ in range(size):
        print("*", end="")
    print()  
    row += 1
