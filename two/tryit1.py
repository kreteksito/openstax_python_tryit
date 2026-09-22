"""Cups of water

This program inputs the number of ounces of water drank by the user and calculates how many cups of water were drank and how many cups are left to drink.
"""
#input ounces of water drank
ounces = int(input())
print('Input ounces:', ounces, ', type:', type(ounces))

# calculate cups drank 'float' and cups left to drink 'int'
cups_drank = ounces / 8
cups_left = int(8 - cups_drank)

#print cups drank 'float' and cups left 'int'
print(cups_drank, 'cups drank, type:', type(cups_drank))
print('About', cups_left, 'cups left to drink, type:', type(cups_left))