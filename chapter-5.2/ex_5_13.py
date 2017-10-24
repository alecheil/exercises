# Programming Exercise 5-13
#
# Program to display a table of times and falling distances for a specific range in seconds.
# This program accepts no input,
# but uses a loop to pass a range of times in seconds to a function
# 	that returns the falling distance for that amount of time,
# and displays the results as a table.

from tables import print_two_column_header


# define the main function
def main():
    # define a local float variable to hold distance
    distance = 0.0

    # Set up results chart, printing time and falling distance separated by a tab
    # include a separator line made with a row of underscores
# time    Distance  <--- somthing like this
#-----------------

    print_two_column_header(" time","distance")
    # loop through a range of time values (in seconds)
    for time in range(10):
        # pass the time to a falling distance function and assign result to distance
        falling_distance = falling_distance(time)
		# print the time and distance formatted to two places, separated by a tab

def print_two_column_header(column_header_1, column_header_2):
    print(column_header_1, "    ",column_header_2)
    print("-------------------")
# Define a function to calculate the falling distance for a time in seconds
# The function accepts a time in seconds as a parameter,
# computes the distance,
# and returns the distance it has fallen in that time
def falling_distance(time):
	# define a local float variable to hold falling distance
	falling_distance = 0.0
	# compute the falling distance using a formula and the time
	falling_distance = 9.8 * time * time
	# return the falling distance
    return(falling_distance)


# Call the main function to start the program

print(__name__)
if __name__ == "__main__":
    main()


