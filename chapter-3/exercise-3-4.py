# Programming Exercise 3-4
#
# Program to convert a number from 1 to 10 to a Roman numeral.
# This program will accept an integer from 1 to 10 from the user
# and use it to choose an appropriate Roman numeral
# to display on the screen.

# Variables to hold a number and a numeral.
# initialize the number as an int and the numeral as a string.
'''
1 = I
2 = II
3 = III
4 = IV
5 = V
6 = VI
7 = VII
8 = VIII
9 = IV
10 = V
'''

# Get number from user and convert it to an int
num = input("enter a number: ")
i_num = int(num)

# Set numeral to a Roman numeral value based on the value of number
# use a set of if ... elif .... etc. statements.
if num == "1":
    print("1 as a Roman Numeral is: I")
elif num == "2":
    print("2 as a Roman Numeral is: II")
elif num == "3":
    print("3 as a Roman Numeral is: III")



# use a final else to display an error if number is out of range.


# display the numeral on the screen.






