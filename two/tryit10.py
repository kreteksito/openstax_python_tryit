"""Cylender formulas"""
# TODO: Add the import statement.
import math
r = float(input("radius? "))
h = float(input("height? "))

area = 0    # TODO: Replace with area formula.
area = math.tau * r * h + math.tau * math.pow(r, 2)
volume = 0  # TODO: Replace with volume formula.
volume = math.pi * math.pow(r, 2) * h

print("Area:", round(area, 2))
print("Volume:", round(volume, 2))