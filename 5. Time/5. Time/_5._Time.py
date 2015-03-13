#First :)



#Please attend our event Sunday, July 20 in the year 1997

import datetime
currentdate = datetime.datetime.today()
#strftime allows you to specify the date format
print (currentdate.strftime
       ("Please attend our event %A, %B %d in the year %Y"))


userInput = input("Please enter your birthday ")
birthday = datetime.datetime.strptime(userInput, "%m/%d/%Y")
print(birthday)

days = birthday - currentdate
print(days)
#print(days.days)

