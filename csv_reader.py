#!/usr/bin/python3

import csv
import os
from os import path

""" AddressBookCSV.py: This program manipulates a csv file containing a contact list
allowing a user to view the contents,  search for strings and add contacts to the file."""

"""Begin Psuedocode"""
# Output List: main_menu(), error_msg, read_file(), yes_or_no(), error_msg, append_file(), search_file

# Input List: read_file(), yes_no, fname, lname, addr, city, state, zip_code, phone_number, search_var

# Module String error_msg()
#     Display "Invalid Input"


# Class Userinput
#     Public Module String usr_input()
#         Declare String fname
#         Declare String lname
#         Declare String addr
#         Declare String city
#         Declare String state
#         Declare String zip_code
#         Declare String phone_number
#         Display "What is the first name? "
#         Input fname
#         Display "What is the last name? "1
#         Input lname
#         Display "What is the street address? "
#         Input addr
#         Display "What is the city? "
#         Input city
#         Display "What is the state? "
#         Input state
#         Display "What is the ZIP code? "
#         Input zip_code
#         Display "What is the phone number? "
#         Input phone_number
#         Return fname, lname, addr, city, state, zip_code, phone_number
#     End Module
#
#     Public Module usr_search()
#         Declare String search_var
#         Display "What are you looking for? "
#         Input search_var
#         Return search_var
#     End Module
# End Class


# Set program_input = Userinput()


# Class Addressbook
#    Public Module csv_file()
#        // Specifies the location csv file. If it exists in the same directory as this program
#        // you can leave this alone. Otherwise, specify the path to the file by changing the 'file_path' variable.
#        Declare String file
#        Set file_path = "./addressbook.csv"
#        Set file = os.path.expanduser(file_path)
#        Return file
#     End Module
#
#     Public Module String read_file()
#         // This reads the csv file.
#         Declare String read_csv
#         Declare String csvfile
#         Set file = csv_file()
#
#         with open(file) as csvfile:
#             Set read_csv = csv.reader(csvfile, delimiter=",")
#             For row in read_csv:
#                 Display row
#             End For
#     End Module
#
#     Public Module String search_file():
#         // This reads the csv file and matches user input with a string in the file.
#         Set search_var = usr_search()
#         Set file = csv_file()
#
#         with open(file) as csvfile:
#             read_csv = csv.reader(csvfile, delimiter=",")
#             For row in read_csv:
#                 For field in row:
#                     If field == search_var:
#                         print(row)
#                     End If
#                 End For
#             End For
#     End Module
#
#     Public Module String append_file()
#         // This appends the csv file.
#         Declare String app_csv
#         Declare String csvfile
#         Set file = csv_file()
#         Set fname, lname, addr, city, state, zip_code, phone_number = usr_input()
#
#         with open(file, "a") as csvfile
#             Set write_csv = csv.writer(csvfile, delimiter=",")
#             write_csv.writerow([fname, lname, addr, city, state, zip_code, phone_number])
#     End Module
# End Class


# Set address_book = Addressbook()


# Module Integer main_menu()
#     // This is the main menu for the program.
#     Declare Integer usr_choice
#     Display(30 * '-')
#     Display " A D D R E S S  B O O K"
#     Display " M A I N - M E N U"
#     Display 30 * "-"
#     Display "1. View File Contents"
#     Display "2. Write to File"
#     Display "3. Quit"

#     // Get user input and make sure it is an integer.
#     Try
#         Display "Enter your choice [1-4] : "
#         Input Integer usr_choice
#     Except
#         Call error_msg()
#     End Try

#     // Take action as per selected menu-option
#     If usr_choice == 1 Then
#         Call address_book.read_file()
#     Else If usr_choice == 2 Then
#        Call address_book.append_file()
#     Else If usr_choice == 3 Then
#        Call address_book.search_file()
#     Else If usr_choice == 4 Then
#         Call quit
#     Else
#         Display "Enter a Number Between 1 and 4. "
#     End If
# End Module


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

"""Begin Python"""

__author__ = "Brian Hurst"


def error_msg():
    print("Invalid Input")


class Userinput:
    def usr_input(self):
        fname = input("What is the first name? ")
        lname = input("What is the last name? ")
        addr = input("What is the street address? ")
        city = input("What is the city? ")
        state = input("What is the state? ")
        zip_code = input("What is the ZIP code? ")
        phone_number = input("What is the phone number? ")
        return fname, lname, addr, city, state, zip_code, phone_number

    def usr_search(self):
        search_var = ""
        search_var = input("What are you looking for? ")
        return search_var


program_input = Userinput()


class Addressbook:
    def csv_file(self):
        """Specifies the location csv file. If it exists in the same directory as this program
        you can leave this alone. Otherwise, specify the path to the file by changing the 'file_path' variable."""
        file = ""
        file_path = "./addressbook.csv"
        if os.path.isfile(file_path):
            print("The file exists and is readable")
        else:
            print("Either the file is missing or it is not readable.")

        file = os.path.expanduser(file_path)
        return file

    def read_file(self):
        """This reads and displays the whole csv file."""
        read_csv = ""
        csvfile = ""
        file = self.csv_file()

        with open(file) as csvfile:
            read_csv = csv.reader(csvfile, delimiter=",")
            for row in read_csv:
                print(row)

    def search_file(self):
        """This reads the csv file and matches user input with a string in the file."""
        search_var = program_input.usr_search()
        file = self.csv_file()

        with open(file) as csvfile:
            read_csv = csv.reader(csvfile, delimiter=",")
            for row in read_csv:
                for field in row:
                    if field == program_input.usr_search().search_var:
                        print(row)

    def append_file(self):
        """This appends the csv file."""
        app_csv = ""
        csvfile = ""
        file = self.csv_file()
        fname, lname, addr, city, state, zip_code, phone_number = program_input.usr_input()

        with open(file, "a") as csvfile:
            write_csv = csv.writer(csvfile, delimiter=",")
            write_csv.writerow([fname, lname, addr, city, state, zip_code, phone_number])

address_book = Addressbook()


def main_menu():
    """ This is the main menu for the program."""
    usr_choice = 0.0
    print((30 * "-"))
    print(" A D D R E S S  B O O K ")
    print(" M A I N - M E N U")
    print((30 * "-"))
    print("1. View File Contents")
    print("2. Write to File ")
    print("3. Search the file")
    print("4. Quit ")

    # ## Get user input and make sure it is an integer. ###
    try:
        usr_choice = int(input("Enter your choice [1-4]: "))
    except ValueError:
        error_msg()

    # ## Take action as per selected menu-option ###
    if usr_choice == 1:
        address_book.read_file()
    elif usr_choice == 2:
        address_book.append_file()
    elif usr_choice == 3:
        address_book.search_file()
    elif usr_choice == 4:
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

