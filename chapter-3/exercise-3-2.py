# Programming Exercise 3-2
#
# Program to find which of two rectangles has the greater area.
# This program will get two sets of lengths and widths from a user,
# use them to calculate and compare two area values,
# and display a message comparing those areas

# Local variables
# you need length, width and area for A and for B
# initialize these as floats

# Get length A from the user and convert it to a float
length_A = input("enter length of A: ")
f_length_A = float(length_A)

# Get width A from the user and convert it to a float
width_A = input("enter width of A: ")
f_width_A = float(width_A)

# Get length B from the user and convert it to a float
length_B = input("enter length of B: ")
f_length_B = float(length_B)

# Get width B from the user and convert it to a float
width_B = input("enter width of B: ")
f_width_B = float(width_B)

# Calculate area A
area_A = (f_length_A * f_width_A)

# Calculate area B
area_B = (f_length_B * f_width_B)

# Print each area, formatting the values to 2 decimal places
print("The area of A is" "{0:.2f}".format(area_A))
print("The area of B is" "{0:.2f}".format(area_B))
# if area A is greater, print "A is greater" message.
if area_A > area_B:
    print("A is greater")
# else if area B is greater, print "B is greater" message.
elif area_A < area_B:
    print("B is greater")
# else print "A and B are equal" message.
elif area_A == area_B:
    print("equal rights for both A and B")
