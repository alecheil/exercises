# this program allows the user to choose various
# geometry calculations from a menu. This program
# imports the circle and rectangle modules.

import x_circle
import x_rectangle

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
        choice = int(input("\nenter your choice: "))
        
        output = handle_choice(choice)
        print(output)
        
            
# the display_menu function displays a menu
def display_menu():
    print(" MENU")
    print("1) area of a circle")
    print("2) circumference of a circle")
    print("3) area of a rectangle")
    print("4) perimeter of a rectangle")
    print("5) quit")
   
def handle_area_circle_choice(): 
    radius = float(input("\nenter the circles radius: "))
    return "\nthe area is: " + \
    str(x_circle.area(radius)) + "\n"
def handle_circumference_of_circle():
    radius = float(input("\nenter the circles radius: "))
    return "\nthe circumference is: " + \
        str(x_circle.circumference(radius)) + "\n"
def handle_area_rectangle_choice():  
        width = float(input("\nenter the rectangle's width: "))
        length = float(input("enter the rectangle's length: "))
        return"\nthe area is: " + \
        str(x_rectangle.area(width, length)) + "\n"
def handle_rectangle_perimeter_choice():
        width = float(input("\nenter the rectangle's width: "))
        length = float(input("enter the rectangle's length: "))
        return "\nthe perimeter is: " + \
        str(x_rectangle.perimeter(width, length)) + "\n"
        
        
def handle_choice(choice):
    # perform the selected area
    if choice == AREA_CIRCLE_CHOICE:
        return handle_area_circle_choice()
    elif choice == CIRCUMFERENCE_CHOICE:
        return handle_circumference_of_circle()
    elif choice == AREA_RECTANGLE_CHOICE:
        return handle_area_rectangle_choice()
    elif choice == PERIMETER_CHOICE:
        return handle_rectangle_perimeter_choice()
    elif choice == QUIT_CHOICE:
        return "\nexiting the program..."
    else:
        return "\nerror: invalid selection\n"
    
main()






