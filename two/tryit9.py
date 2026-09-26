"""The quadratic formula"""

# TODO: Add the import statement.
import math

a = float(input("Value of a? "))
b = float(input("Value of b? "))
c = float(input("Value of c? "))
print()
x1 = 0  # TODO: Replace with plus formula.
x1 = (-b + math.sqrt(math.pow(b, 2) -4 * a * c)) / (2 * a)
x2 = 0  # TODO: Replace with minus formula.
x2 = (-b - math.sqrt(math.pow(b, 2) -4 * a * c)) / (2 * a)
print("Solutions:", x1, "and", x2)