#!/usr/bin/python env
"""Write a Python program which accept the user's first and last name and print them in reverse order with a space between them"""

surname = input("Please insert your surname:")
name = input("Please insert your first name:")
print ("Hi " + str(surname)[::-1] + " " + str(name)[::-1])


