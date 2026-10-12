"""Friday Boolean

"It's Friday, I'm in love" —from "Friday I'm in Love," a song released by the Cure in 1992.
Write a program that reads in the day of the week. Assign the Boolean variable, in_love, 
with the result of whether the day is Friday or not."""
# Read in day 
day = input("what day is today?: ")
in_love = ("Friday" == day)# Compute boolean
print("It's", day, "I'm in love?", in_love)