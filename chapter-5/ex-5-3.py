# Programming Exercise 5-3
#
# Program to compute recommended insurance to carry on an item.
# This program accepts a replacement cost from a user,
# calculates a minimum recommended insurance to carry from a global constant,
# then passes these values to a function to be displayed



# Global constant for the percent of replacement cost to insure

PERCENTAGE_OF_REPLACEMENT = float(.50)

# Define the main function
def main():
    # Define local float variables for replacement cost and minimum insurance
    replacement_cost = float()

    # Get the replacement cost from the user
    replacement_cost = float(input("what is the total replacement cost?:  "))

    # Calculate the minimum insurance amount using the global constant
    min_insurance = replacement_cost * PERCENTAGE_OF_REPLACEMENT

    # Call the function to display the insurance details, 
    # passing the replacement cost and minimum insurance to the function
    insurance_details(replacement_cost, min_insurance)

      
# Define a function to display the insurance details
def insurance_details(replacement_cost, min_insurance):
# This function accepts the replacement cost and minimum insurance as parameters,
# uses the global constant to calculate percent insured,
# and displays the insurance details.

	# display the replacement cost, formatting the value to 2 decimal places
    print("replacement cost is: $",format(replacement_cost, '.2f'))
    # display the percent insured, formatting the value to 2 decimal places
    print("percent insured is: 50%")
	# display the minimum insurance, formatting the value to 2 decimal places
    print("minimum insurance is: $",format(min_insurance, '.2f'))


# Call the main function to start the program

main()