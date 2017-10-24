# this program allows the user to choose various
# geometry calculations from a menu. This program
# imports the circle and rectangle modules.

import circle
import rectangle

# constants for the menu choices
AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_CHOICE = 4
QUIT_CHOICE = 5

# the main function
def main():
    # the choice variable controls the loop
    # and holds the users menu choice
    choice = 0
    
    while choice != QUIT_CHOICE:
        # display the menu
        display_menu()
        
        # get the users choice
        choice = int(input("enter your choice: "))
        
        # perform the selected area
        if choice == AREA_CIRCLE_CHOICE:
            radius = float(input("enter the circles radius: "))
            print("the area is: ", circle.area(radius))
        elif choice == CIRCUMFERENCE_CHOICE:
            radius = float(input("enter the circles radius: "))
            print("the circumference is: ", \
                circle.circumference(radius))
        elif choice == AREA_RECTANGLE_CHOICE:
            width = float(input("enter the rectangle's width: "))
            length = float(input("enter the rectangle's length: "))
            print("the area is: ", rectangle.area(width, length))
        elif choice == PERIMETER_CHOICE:
            width = float(input("enter the rectangle's width: "))
            length = float(input("enter the rectangle's length: "))
            print("the perimeter is: ", rectangle.area(width, length))
        elif choice == QUIT_CHOICE:
            print("exiting the program...")
        else:
            print("error: invalid selection")
            
# the display_menu function displays a menu
def display_menu():
    print(" MENU")
    print("1) area of a circle")
    print("2) circumference of a circle")
    print("3) area of a rectangle")
    print("4) perimeter of a rectangle")
    print("5) quit")
    
main()






