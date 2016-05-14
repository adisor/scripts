#!/usr/bin/python env
""" Write a Python program to accept a filename from the user print the extension of that.
Sample filename : abc.java
Output : java"""

filename = input("Please insert the filename:")

extension = filename.split(".")

print (extension[1])
