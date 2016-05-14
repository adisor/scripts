#!/usr/bin/python env
"""Write a Python program to display the examination schedule. (extract the date from exam_st_date)
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014"""

#exam_st_day = input("Please insert the day for the exam:")
#exam_st_month = input("Please insert the month for the exam:")
#exam_st_year = input("Please insert the year for the exam:")

#print ("The examination will start from :" + str(exam_st_day) + " / " + str(exam_st_month) + " / " + str(exam_st_year))

exam_st_date = (11,12,2014)  
print( "The examination will start from : %i / %i / %i"%exam_st_date)  
