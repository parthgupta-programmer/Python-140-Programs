# Program 8
# Write a Python Program to display Calender.


import calendar

month=int(input("Enter the month:"))
year=int(input("Enter the year:"))

cal=calendar.month(year,month) # Return a month's calendar string (multi-line).
print(cal)

# Output : 

# Enter the month:8 
# Enter the year:2025
#     August 2025
# Mo Tu We Th Fr Sa Su
#              1  2  3
#  4  5  6  7  8  9 10
# 11 12 13 14 15 16 17
# 18 19 20 21 22 23 24
# 25 26 27 28 29 30 31