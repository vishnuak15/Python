#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


# construct a basic timedelta and print it
print(timedelta(days=365, hours=5, minutes=1))

# print today's date
now = datetime.now()
print("today is:"+str(now))

# print today's date one year from now
print("one year from now it will be:"+ str(now+timedelta(days=365)))

# create a timedelta that uses more than one argument
print("In 2 days and 3 weeks, it will be:"+str(now+timedelta(days=2,weeks=3)))

# calculate the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks=1)  
s = t.strftime("%A %B %d, %Y")
print("One weeks ago it was:"+s)

### How many days until April Fools' Day?
today = date.today()
aft = date(today.year, 4,1)

# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if aft < today:    
    print("April Fool's Day is already went by %d days ago"%((today-aft).days))
    aft = aft.replace(year = today.year+1)

# Now calculate the amount of time until April Fool's Day  
time_to_aft = aft-today
print("Its just", time_to_aft.days, "days until April Fools day")
