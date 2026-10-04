""" Spaced out

The following code works correctly but is formatted poorly. In particular, the code does not include spaces 
recommended by PEP 8. Furthermore, two of the lines are about 90 characters long. Reformat the code to follow 
the guidelines in this section. Be careful not to change the behavior of the code itself."""

adj1 = input("Adjective: ")
adj2 = input("Adjective: ")
noun1 = input("Noun: ")
noun2 = input("Noun: ")
x = int(input("Integer: "))
y = int(input("Integer: "))
z = int(input("Integer: "))
print()
print("A vacation is when you take a trip to some", adj1, "place with your", adj2, "family.")
print("Usually you go to some place that is near a/an", noun1, "or up on a/an", noun2 + ".")
print("To be worthwhile, you should travel at least", x**3 + y**3 + z**3, "kilometers away.")
