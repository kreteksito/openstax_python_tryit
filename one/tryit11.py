"""The calculation of the force of gravity.

Greets the user and calculates the gravitational force between Earth and a person.
Author: Juan Carlos Mamani Mamani

"""
name = input("What is your name? ")
print("Hello,", name + "!")

# mass of the planet earth
m1 = 5.98e24
# mass of a person (in kg)
m2 = 70
# distance from earth's center
r = 6.38e6

# gravitational constant
G = 6.674e-11
# Newton's law of universal gravitation
F = G * (m1 * m2) / r**2

print("The force of gravity is", F, "Newtons")