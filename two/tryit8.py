# Read the input.
total = float(input("Total amount? "))
cash = int(input("Cash payment? "))

# TODO: Calculate change.
change = round((cash-total), 2)
print()
print("Change due $", change)
change = int(change*100)

# TODO: Print the results.
print()
print("  Dollars:", change // 100)
change = change % 100
print(" Quarters:", change // 25)
change = change % 25
print("    Dimes:", change // 10)
change = change % 10
print("  Nickels:", change // 5)
change = change % 5
print("  Pennies:", change // 1)



#change = round((cash-total), 2)
#cents = round(change*100)

#dollar = cents // 100
#quarter = cents % 100 // 25
#dime = cents % 100 // 10
#nickel = cents % 100 % 5 // 5
#penny = cents % 100 % 5 // 1

# TODO: Print the results.
#print()
#print("  Dollars:", dollar)
#print(" Quarters:", quarter)
#print("    Dimes:", dime)
#print("  Nickels:", nickel)
#print("  Pennies:", penny)

