# ParkingMeter.py
# @ author: A. N. Other
# date: September 2016

from tkinter import *
app = Tk()
app.mainloop()
print ("Kia Ora, this is a parking meter")
park_time = 4
print ("park_time time is ", park_time, " hours.")

rate = 4
cost = 0

if park_time > 3:
    cost = rate *3
    rate -= 2 # drop the rate by $2
    park_time -= 3 # get the remainder of the parking time
    cost += rate * park_time # add to the current cost
    print("The cost of the parking is $", cost)
else:
    cost = rate * park_time
    print ("The cost of the parking is $", cost)

#test case assertion
#park_time = 4
#total cost of parking = $14
