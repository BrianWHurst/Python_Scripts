#!/usr/bin/python3

"""Geometry.py: Calculate the area of a triangle,
rectangle,trapezoid, and the volume of a sphere using a menu to get
input from the user."""

# Output list: triangle_area, rectangle_area, trap_area, sphere_vol
# error_msg, error_msg2, yes_or_no, main_menu

# Input list: usr_choice, triangle_base, triangle_height, yes_no,
# rectangle_length, rectangle_width, base_one, base_two, trap_height,
# radius

# Module String error_msg()
#     Display "Invalid Input, try again."


# Module String error_msg2()
#     Display "Number must be greater than zero.")


# Module Real area_of_triangle()
#     // This function calculates the area of a triangle.
#     Declare Real triangle_base
#     Declare Real triangle_height
#     Declare Real triangle_area
#     While True
#         Try
#             Display "Enter the base of the triangle: "
#             Input triangle_base
#             If triangle_base <= 0
#                 Call error_msg()
#                 Continue
#             End If
#         Except
#             Call error_msg()
#         Else
#             Break
#     End While
#     While True
#         Try
#             Display "Enter the height of the triangle: "
#             Input triangle_height
#             If triangle_height <= 0
#                 Call error_msg()
#                 Continue
#             End If
#         Except
#             Call error_msg()
#         Else
#             Break
#     End While
#     Set triangle_area = 1/2 * (triangle_base * triangle_height)
#     Display "The area of the triangle is : ", triangle_area
# End Module


# Module Real area_of_rectangle()
#     // This function calculates the area of a rectangle.
#     Declare Real rectangle_length
#     Declare Real rectangle_width
#     Declare Real rectangle_area
#     While True
#         Try
#             Display "Enter the length of a rectangle: "
#             Input rectangle_length
#             If rectangle_length <= 0
#                 Call error_msg()
#                 Continue
#             End If
#         Except
#             Call error_msg()
#         Else
#             Break
#     End While
#     While True
#         Try
#             Display "Enter the width of a rectangle: "
#             Input rectangle_width
#             If rectangle_width <= 0
#                 Call error_msg()
#                 Continue
#             End If
#         Except
#             Call error_msg()
#         Else
#             Break
#     End While
#     Set rectangle_area = rectangle_length * rectangle_width
#     Display "The area of the rectangle is : ", rectangle_area
# End Module


# Module Real area_of_trapezoid
#     // This function calculates the area of a trapezoid.
#     Declare Real base_one
#     Declare Real base_two
#     Declare Real trap_height
#     While True
#         Try
#             Display "Enter base 1 of the trapezoid: "
#             Input base_one
#             If base_one <= 0
#                 Call error_msg()
#                 Continue
#             End If
#         Except
#             Call error_msg()
#         Else
#             Break
#     End While
#     While True
#         Try
#             Display "Enter base 2 of the trapezoid: "
#             Input base_two
#             If base_two <= 0
#                 Call error_msg()
#                 Continue
#             End If
#         Except
#             Call error_msg()
#         Else
#             Break
#     End While
#     While True
#         Try
#             Display "Enter the height of the trapezoid: "
#             Input trap_height
#             If trap_height <= 0
#                 Call error_msg()
#                 Continue
#             End If
#         Except
#             Call error_msg()
#         Else
#             Break
#     End While
#     Set trap_area = (base_one + base_two) / 2 * trap_height
#     Display "The area of the trapezoid is: ", trap_area
# End Module


# Module Real vol_of_sphere
#     // This function calculates the volume of a sphere.
#     Declare Real radius
#     Declare Real sphere_vol
#     While True
#         Try
#             Display "Enter the radius of the sphere: "
#             Input radius
#             If radius <= 0
#                 Call error_msg()
#                 Continue
#             End If
#         Except
#             Call error_msg()
#         Else
#             Break
#     End While
#     sphere_vol = (4 * math.pi * radius ** (3)) / 3
#     Display "The volume of the sphere is: ", sphere_vol)


# Module Integer main_menu()
#     // This is the main menu for the program.
#     Declare Integer usr_choice
#     Display(30 * '-')
#     Display " G E O M E T R Y  P R O G R A M"
#     Display "   M A I N - M E N U"
#     Display 30 * "-"
#     Display "1. Are of a Triangle"
#     Display "2. Area of a Rectangle"
#     Display "3. Area of a Trapezoid"
#     Display "4. Volume of a Sphere"
#     Display "5. Exit"
#     Display 30 * "-"
#     // Get user input and make sure it is an integer.
#     Try
#         Display "Enter your choice [1-4] : "
#         Input Integer usr_choice
#     Except
#         Call error_msg()
#     End Try

#     // Take action as per selected menu-option
#     If usr_choice == 1 Then
#         Call area_of_triangle()
#     Else If usr_choice == 2 Then
#         Call area_of_rectangle()
#     Else If usr_choice == 3 Then
#         Call area_of_trapezoid()
#     Else If usr_choice == 4 Then
#         Call vol_of_sphere()
#     Else If usr_choice == 5 Then
#         Call quit
#     Else
#         Display "Enter a Number Between 1 and 5. "
#     End If


# Module String yes_or_no()
#     // Ask user if they want to return to the menu.
#     Declare String yes_no
#     While yes_no != "No"
#         Display "Would you like to return to the Main Menu? Yes/No: "
#         Input yes_no
#         If yes_no == "Yes" Then
#             Call main_menu()
#         Else If  yes_no == "No" Then
#             print("Exiting")
#         Else
#             Call error_msg()
#         End If
#     End While
# End Module


# Call main_menu()

# Call yes_or_no()

import math


"""Begin Python"""

__author__ = "Brian Hurst"


def error_msg():
    print("Invalid Input, try again.")


def error_msg2():
    print("Number must be greater than zero.")


def area_of_triangle():
    """ This function calculates the area of a triangle."""
    triangle_base = 0.0
    triangle_height = 0.0
    triangle_area = 0.0
    while True:
        try:
            triangle_base = float(input("Enter the base of the triangle: "))
            if triangle_base <= 0:
                error_msg2()
                continue
        except ValueError:
            error_msg()
        else:
            break
    while True:
        try:
            triangle_height = float(input("Enter the height of the triangle: "))
            if triangle_height <= 0:
                error_msg2()
                continue
        except ValueError:
            error_msg()
        else:
            break
    triangle_area = 1 / 2 * (triangle_base * triangle_height)
    print("The area of the triangle is: ", triangle_area)


def area_of_rectangle():
    """ This function calculates the area of a rectangle."""
    rectangle_length = 0.0
    rectangle_width = 0.0
    rectangle_area = 0.0
    while True:
        try:
            rectangle_length = float(input("Enter the length of a rectangle: "))
            if rectangle_length <= 0:
                error_msg2()
                continue
        except ValueError:
            error_msg()
        else:
            break
    while True:
        try:
            rectangle_width = float(input("Enter the width of a rectangle: "))
            if rectangle_width <= 0:
                error_msg2()
                continue
        except ValueError:
            error_msg()
        else:
            break
    rectangle_area = rectangle_length * rectangle_width
    print("The area of the rectangle is : ", rectangle_area)


def area_of_trapezoid():
    """ This function calculates the area of a trapezoid."""
    base_one = 0.0
    base_two = 0.0
    trap_height = 0.0
    trap_area = 0.0
    while True:
        try:
            base_one = float(input("Enter base 1 of the trapezoid: "))
            if base_one <= 0:
                error_msg2()
                continue
        except ValueError:
            error_msg()
        else:
            break
    while True:
        try:
            base_two = float(input("Enter base 2 of the trapezoid: "))
            if base_two <= 0:
                error_msg2()
                continue
        except ValueError:
            error_msg()
        else:
            break
    while True:
        try:
            trap_height = float(input("Enter the height of the trapezoid: "))
            if trap_height <= 0:
                error_msg2()
                continue
        except ValueError:
            error_msg()
        else:
            break
    trap_area = (base_one + base_two) / 2 * trap_height
    print("The area of the trapezoid is: ", trap_area)


def vol_of_sphere():
    """ This function calculates the volume of a sphere. """
    radius = 0.0
    sphere_vol = 0.0
    while True:
        try:
            radius = float(input("Enter the radius of the sphere: "))
            if radius <= 0:
                error_msg2()
                continue
        except ValueError:
            error_msg()
        else:
            break
    sphere_vol = (4 * math.pi * radius ** 3) / 3
    print("The volume of the sphere is: ", sphere_vol)


def main_menu():
    """ This is the main menu for the program."""
    usr_choice = 0.0
    print((30 * "-"))
    print(" G E O M E T R Y  P R O G R A M")
    print("   M A I N - M E N U")
    print((30 * "-"))
    print("1. Area of a Triangle")
    print("2. Area of a Rectangle")
    print("3. Area of a Trapezoid")
    print("4. Volume of a Sphere")
    print("5. Exit")
    print((30 * "-"))
    # ## Get user input and make sure it is an integer. ###
    try:
        usr_choice = int(input("Enter your choice [1-4]: "))
    except ValueError:
        error_msg()

    # ## Take action as per selected menu-option ###
    if usr_choice == 1:
        area_of_triangle()
    elif usr_choice == 2:
        area_of_rectangle()
    elif usr_choice == 3:
        area_of_trapezoid()
    elif usr_choice == 4:
        vol_of_sphere()
    elif usr_choice == 5:
        quit()
    else:
        print("Enter a Number Between 1 and 5. ")


def yes_or_no():
    """ Ask user if they want to return to the menu."""
    yes_no = ""
    while yes_no != "No":
        yes_no = input("Would you like to return to the menu? Yes/No: ")
        if yes_no == "Yes":
            main_menu()
        elif yes_no == "No":
            print("Exiting")
        else:
            error_msg()


main_menu()

yes_or_no()
