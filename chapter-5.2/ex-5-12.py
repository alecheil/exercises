# Programming Exercise 5-12
#
# Program to find the greater of two integers.
# This program accepts two integers,
# passes them to a function that compares them,
# and displays which one is greater.



# define the main function
def main():
    
    # Define local variables to hold two integers
    first_integer = 0
    second_integer = 0

    # prompt the user for the first integer
    first_integer = int(input("enter first integer: "))
    
    # prompt the user for the second integer
    second_integer = int(input("enter second integer: "))

    # print the return value from calling a function to find the greater of two integers
    # the two integers are passed as arguments
    greater(first_integer, second_integer)
    #print(this_one)
 
# Define a function to compare integer values.
# This function accepts two integer parameters,
# compares them,
# and returns the value of the greater.
def greater(first,second):
	# if the first integer is greater, return the first integer
    if first > second:
        print("integer one is greater than integer two")
        return first
	# else, return the second integer
    else: 
        print("integer two is greater than integer one")
        return second

# Call the main function to start the program




main()
