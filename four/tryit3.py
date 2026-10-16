"""Converting temperature units

The following program reads in a temperature as a float and the unit as a string: 'f' for Fahrenheit or 'c' for Celsius

Calculate new_temp, the result of converting temp from Fahrenheit to Celsius or Celsius to Fahrenheit based on unit. 
Calculate new_unit: 'c' if unit is 'f' and 'f' if unit is 'c'.
Conversion formulas:
- Degrees Celsius = (degrees Fahrenheit - 32) * 5/9
- Degrees Fahrenheit = (degrees Celsius * 9/5) + 32"""
temp = float(input())
unit = input() # f for Fahrenheit or c for Celsius
if unit == "f":
    new_temp = (temp - 32) * 5/9 
    new_unit = "c"
else:
    new_temp = (temp * 9/5) + 32
    new_unit = "f"
       

print(temp, unit, "is converted to", new_temp, new_unit)