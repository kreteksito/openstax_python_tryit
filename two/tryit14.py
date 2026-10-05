"""Tip calculator

"""
percent_to_tip = float(input("Percentage to tip: "))
num_people = int(input("Number of people: "))
bill_amount = float(input("Enter bill amount: "))

#output values
#print("  Enter bill amount:", bill_amount)
#print("  Percentage to tip:", percent_to_tip)
#print("  Number of people:", num_people)

#calculate tip amount and total amount
tip_amount = bill_amount * percent_to_tip / 100
total_amount = bill_amount + tip_amount
print()
#output total price
print("Tip amount: $" + str(round(tip_amount, 2)))
print("Total amount: $" + str(round(total_amount, 2)))
print()
#output price per person
print("Tip per person: $" + str(round(tip_amount / num_people, 2)))
print("Total amount: $" + str(round(total_amount / num_people, 2)))
