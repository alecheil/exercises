# Programming Exercise 6-1
#
# Program to display the contents of a text file.
# This program takes no user input, but requires a numbers.txt file,
# opens the fine and reads the whole contents at once,
# and displays the contents.


# define the main function
def main():
    # Declare a local variable to hold the file contents
    # initialize it as an empty string
    file_contents = ""
    file_name = ""
    # Open numbers.txt file for reading
    # that is, use a variable to hold the file handle created when opening the file
    file_name = open("numbers.txt","r")

    # Read in data and store its contents
    file_contents = file_name.read()

    # Close file
    file_name.close()

    # Print the contents
    print(file_contents)

# Call the main function.


main()