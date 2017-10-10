# Programming Exercise 3-6
#
# Program to check if a date is 'magic' (day * month = year).
# This program takes a month, day and year from the user as integers,
# Checks to see if each is in range, then checks whether month * day = year,
# then displays an appropriate message depending on the result

# Variables for month, day, year and message
# initialize month, day and year as integers, message as a string
<<<<<<< HEAD
month = input("What is the month? (mm)" )
day = input("What is the day? (dd)" )
year = input("what is the year?(yy)" )

# Get month and cast it to int
month = int(month)

# Get day and cast it to int
day = int(day)

# Get year and cast it to int
year = int(year)

# This problem can be solved with if-else logic by the reducing the problem domain
# if month input is out of range
if month < 1 and month > 12:
	# set message to hold "invalid month" message
    print("invalid month")

# else if day input is out of range
elif day < 1 and day > 30:
    # set message to hold "invalid day" message
    print("invalid day")
    
# else if  year input is out of range (greater than 99 or less than 0)
elif year < 0 and year > 99:
    # set message to hold "invalid year" message
    print("invalid year")
    
# else 
# else:
    # set message to hold the date in 00/00/00 form
    # date = ("day/month/year")
    # print(date)
    
        # if day * month equals year, add " is a magic date" to message
if day * month == year:
    print(" is a magic date")
    # else add " is not a magic date" to message
else:
    print(" is not a mgic date")

# print message for the user

=======


# Get month and cast it to int


# Get day and cast it to int


# Get year and cast it to int


# This problem can be solved with if-else logic by the reducing the problem domain
# if month input is out of range

	# set message to hold "invalid month" message


# else if day input is out of range

    # set message to hold "invalid day" message

# else if  year input is out of range (greater than 99 or less than 0)

    # set message to hold "invalid year" message

# else 

    # set message to hold the date in 00/00/00 form
    
    # if day * month equals year, add " is a magic date" to message
    
    # else add " is not a magic date" to message


# print message for the user


>>>>>>> upstream/master
