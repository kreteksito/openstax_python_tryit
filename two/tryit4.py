"""Print n times

The program print concatenation of strings n times 
"""
#prompt to strings and an integer
str1 = input("Enter a string: ")
str2 = input("Enter a string: ")
count = int(input("Enter a integer to print n times: "))

#concatenation two string with '\' new line at the end of the string
result = str1 + " " + str2 + "\n"

#print n times of the concatenation of strings
print(count * result)