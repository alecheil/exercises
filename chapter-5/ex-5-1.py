# Programming Exercise 5-1
#
# Program to convert kilometers to miles.
# This program accepts a distance in kilometers from the user,
# passes it to a function, which calculates its value in miles
# and displays the result for the user.


# Global constant for the ratio of kilometers to miles
MILES_PER_KM = 1.60934

# define the main function
def main():

    # Define a local float variable to hold the distance in kilometers
    dist = 0.0
    
    # Get distance in kilometers from the user
    dist = float(input("enter distance in KM: "))

    # pass the distance in kilometers to a function to convert to miles
    convert_km_miles(dist)


# define the function to convert to miles
# the function takes kilometers as an argument
# calculates the equivalent number of miles
# and prints the result
def convert_km_miles(distance_km): 
    # print("ldldl" + str(distance_km))

    # Define a local float variable for miles
    distance_mi = 0.0
    
	# use the global conversion constant to compute miles    
    distance_mi = MILES_PER_KM * distance_km
    
    # print the results, formatting float values to 2 decimal places
    formatted_mi = format(distance_mi, '.2f')
    print("you have taveled",formatted_mi, "miles")


# Call the main function to start the program

main()
