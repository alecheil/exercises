# Programming Exercise 3-1
#
# Program to display the name of a week day from its number.
# This program prompts a user for the number (1 to 7)
# and uses it to choose the name of a weekday
# to display on the screen.

# Variables to hold the day of the week and the name of the day.
# Be sure to initialize the day of the week to an int and the name as a string.


# Get the number for the day of the week.
# be sure to format the input as an int
day_number = input("enter day of the week as a number (1-7): ")

# Determine the value to assign to the day of the week.
# use a set of if ... elif ... etc. statements to test the day of the week value.
if day_number == 1:
    print("sunday")
elif day_number == 2:
    print("monday")
elif day_number == 3:
    print("tuesday")
elif day_number == 4:
    print("wednesday")
elif day_number == 5:
    print("thursday")
elif day_number == 6:
    print("friday")
elif day_number == 7:
    print("saturday")
elif day_number > 7:
    print("error 420: number too high")




# use the final else to display an error message if the number is out of range.


# display the name of the day on the screen.




