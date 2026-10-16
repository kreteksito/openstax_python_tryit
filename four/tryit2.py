"""Improved division

The following program divides two integers. Division by 0 produces an error.
Modify the program to read in a new denominator (with no prompt) in the denominator is 0."""

num = int(input())
den = int(input())
 #f den == 0:

 #   print("The denominator must not be zero, try again.")
#else:
 #   result = num / den
 #   print(result)
if den == 0:
    den = int(input())

result = num / den
print(result)

