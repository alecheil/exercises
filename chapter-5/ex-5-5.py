# Programming Exercise 5-5
#
# Program to compute assessed value and property tax.
# This program accepts a property value from a user,
# uses global constants to calculate an assessed value and property tax,
# then passes them to a function to display the results for the user.



# Global constants for assessment percentage and property tax rate
ASSESSMENT_PERCENTAGE = float(0.08)
TAX_RATE = float(0.014)

# define the main function
def main():
    # Define local float variables for property value, assessed value and property tax
    property_value = float()
    assessed_value = float()
    property_tax = float()

    # Get the property value from the user.
property_value = input("enter the property value: ")

    # Calculate the assessed value using the global constant
assessed_value = property_value * ASSESSMENT_PERCENTAGE

    # Calculate the property tax using the global constant
property_tax = property_value * TAX_RATE

    # Call the function to display property tax information, 
    # passing assessed value and property tax as arguments
property_tax_info(assessed_value, property_value)

    
# Define a function to display property tax information.
# This function accepts the assessed value and property tax as parameters,
# performs no calculations,
# but displays the information with float variables formatted to 2 decimal places.
def property_tax_info(assessed_value, property_value):

	# display the assessed value
    print("your assessed property value is: ", format(assessed_value, '2f'))
	# display the property tax
    print("your property tax is: ", format(property_tax, '.2f'))


# Call the main function to begin the program.

main()