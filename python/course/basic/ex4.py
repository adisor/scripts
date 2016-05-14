#!/usr/bin/python env
"""Write a Python program which accept the radius of a circle from the user and compute the area.
Sample Output :
r = 1.1
Area = 3.8013271108436504"""


from math import pi  
r = float(input ("Input the radius of the circle : "))  
print ("The area of the circle with radius " +  str(r) + " is: " + str(pi * r**2))  
