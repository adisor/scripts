#!/usr/bin/python env
"""Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'bad' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
Sample String : 'The lyrics is not that poor!'
Expected Result : 'The lyrics is good!'"""
def not_poor(str1):  
      snot = str1.find('not')  
      sbad = str1.find('poor')  
      
      if sbad > snot: 
        str1 = str1.replace(str1[snot:(sbad+4)], 'good')  
      
     return str1  
print(not_poor('The lyrics is not that poor!'))  
