"""Backing bread

"""

#inputs
bread_weight = float(input("Bread weight: "))
serving_size = float(input("Serving size: "))
num_guests = int(input("Numer guests: "))

#calculate the # of loaves
loaves = num_guests * serving_size / bread_weight

print()
#output total loaves
print("  For", num_guests, "people, you will need", loaves, "loaves of bread: ")

#output total of each ingredient
print("   ", 1.5*loaves, "teaspoons instant yeast")
print("   ", 1.5*loaves, "teaspoons salt")
print("   ", 1.5*loaves, "teaspoons sugar")
print("   ", 2.5*loaves, "cups all-purpose flour")
print("   ", 2*loaves, "cups sourdough starter")
print("   ", 0.5*loaves, "cups lukewarm water")

