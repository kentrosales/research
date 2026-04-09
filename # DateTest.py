from datetime import datetime
from datetime import timedelta

date_input = input("Please enter you DOB in the format Mmm DD YYYY: \n")
date_object = datetime.strptime(date_input, '%b %d %Y')

print("The year entered is ", date_object.month,
      date_object.day, date_object.year, "\n")
