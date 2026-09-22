"""Product as float

The following program reads two integers in as strings that calculate the product of the two integers, and print the result as a float
"""

x = input("Enter the first integer: ")
y = input("Enter the second integer: ")

#Convert two strings to integers and calculate their product
product = int(x) * int(y)

print()

# print the product as a float
print(float(product))