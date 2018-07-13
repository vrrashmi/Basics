#Date and time program
#Date : 13th July,2018
import datetime
from datetime import date
from datetime import timedelta
v=timedelta(microseconds=-1)    #to get current time
t=datetime.time(1,2,3)          #random time
now=date.today()                #current date
bd=date(1998,2,16)              #random birth date
c=now-bd                        #difference of dates and time together

#print all values
print("Current time : ",v)
print("Date now  : ",now)   
print("Hour      : ",t.hour)
print("Minutes   : ",t.minute)
print("Seconds   : ",t.second)
print("Current Time    :",v)
print("Date and time difference : ",c)

