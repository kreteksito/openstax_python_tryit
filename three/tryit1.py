"""Shift cipher

The program use indexes and unicode. to generate secret text output.""" 

w = input("Enter 3-letter word: ")
s = int(input("Shift by how many letters? "))

#shift the letters
m = (chr(ord(w[0]) + s))
m1 = (chr(ord(w[1]) + s))
m3 = (chr(ord(w[2]) + s))
#output the secret message
print()
print("The secret message is: ",m + m1 + m3)
