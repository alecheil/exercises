# Programming Exercise 2-3
#
# Program to convert area in square feet to acres.
# This program will prompt a user for the size of a tract in square feet,
# then use a constant ratio value to calculate it value in acres
# and display the result to the user.

# Variables to hold the size of the tract and number of acres.
# be sure to initialize these as floats




# Constant for the number of square feet in an acre.
#def FEET_IN_ACRE_1():
FEET_IN_ACRE = 43560
FEET_IN_ACRE = float(FEET_IN_ACRE)

# Get the square feet in the tract from the user.
# you will need to convert this input to a float

tract_feet = input("size of tract in square feet")
tract_feet = float(tract_feet)

# Calculate the number of acres.

tract_acres = tract_feet / FEET_IN_ACRE
tract_acres = float(tract_acres)

# Print the number of acres.
# remember to format the acres to two decimal places

print(tract_acres)



