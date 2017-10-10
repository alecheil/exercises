# Programming Exercise 3-3
#
# Program to assign an age category to an numerical age.
# This program will prompt the user for an integer age value,
# and use it to choose an age category,
# then display that category on the screen.

# Variables to hold an age and a category.
# initialize age as an int and category as a string.
#infant = 0-1
#child = 2-12
#teenager = 13-17
#adult = 18-122

# Get the person's age.
# remember to convert the input to an int.
age = input("enter your age: ")
i_age = float(age)

# Determine if the person is an infant, child, teenager, or adult and set the category.
# Use a series of if ... elif ... etc. statements.
if age <= 1:
    print("you are an infant")
elif age <= 12:
    print("you are a child")
elif age <= 17:
    print("you are a teenager")
elif age <= 122:
    print("you are an adult")
elif age > 122:
    print("you either set a new record, or you're dead...")




# display a message with the age category.



