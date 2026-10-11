"""Creating a tuple from a list

Suppose a programmer wants to create a tuple from a list to prevent future changes. 
The tuple() function creates a tuple from an object like a list. Ex: my_tuple = tuple(my_list) 
creates a tuple from the list my_list. Update the program below to create a tuple final_grades 
from the list grades."""

grades = [68, 77, 81, 73]
grades[0] += 5

final_grades = tuple(grades)
print(f'final_grades: {final_grades} is a {type(final_grades)}')
print(grades)