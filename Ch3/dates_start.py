#
# Example file for working with date information
#
from datetime import date,time,datetime

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = date.today()
  print("Todays date is ",today)
  print("Today's date is ",today.day,today.month,today.year)
  # print out the date's individual components
  print("Todays week day",today.weekday())
  days=['monday','tuesday','wednsday','thursday','friday','saturday','sunday']
  print("Todays date is:",days[today.weekday()])
  # retrieve today's weekday (0=Monday, 6=Sunday)

  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  today = datetime.now()
  print("The current datetime is:",today)
  
  # Get the current time
  t=datetime.time(datetime.now())
  print(t)
 

  
if __name__ == "__main__":
  main();
  