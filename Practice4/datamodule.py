#creating a data object ---
from datetime import date
d = date(1996, 12, 11)
print(d)


#get current date ---
from datetime import date
t = date.today()
print(t)


#Accessing Year, Month and Day Attributes ---
from datetime import date
t = date.today()
print(t.year)
print(t.month)
print(t.day)



#Create Date from Timestamp ---




#Convert Date to String ---
from datetime improt date
t = date.today()
date_str = t.isoformat()
print(date_str)
print(type(date_str))



#timeclass ---
#Example 1: Time object representing time in Python ---
from datetime import time

# Create time object with hour, minute and second
my_time = time(13, 24, 56)
print("Entered time:", my_time)

# Time object with only minute specified
my_time = time(minute=12)
print("Time with one argument:", my_time)

# Time object with default (00:00:00)
my_time = time()
print("Time without argument:", my_time)

# time(hour=26)      → ValueError: hour must be in 0..23
# time(hour='23')    → TypeError: string passed instead of int

'''Example 3: Convert Time object to String

We can convert time object to string using isoformat() method.'''

from datetime import time

# Creating Time object
Time = time(12,24,36,1212)

# Converting Time object to string
Str = Time.isoformat()
print("String Representation:", Str)
print(type(Str))




#Example 3: Current date and time ---
from datetime import datetime

# Calling now() function
today = datetime.now()
print("Current date and time is", today)



#Example 4: Convert Python Datetime to String ---
from datetime import datetime as dt

# Getting current date and time
now = dt.now()
string = dt.isoformat(now)
print(string)
print(type(string))



