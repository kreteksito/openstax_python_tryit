"""Even numbers

Write a program that reads in an integer and prints whether the integer is even or not. 
Remember, a number is even if the number is divisible by 2. 
To test this use number % 2 == 0. Ex: If the input is 6, the output is "6 is even: True"."""

#create variable
number = int(input("Enter a number: "))

# bolean if number are even or not
even = number % 2 == 0

# print if number is even
print(f"Is the number {number} even? ", even)


