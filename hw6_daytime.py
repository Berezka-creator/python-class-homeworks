# #Homework  6
# Demonstrate the use of a generator that indicates for each event in access_log
# the number of seconds elapsed since the most recent midnight
from datetime import datetime
from datetime import date
import re

today = date.today()
midnight = datetime(today.year,today.month, today.day)

time_stamp =(re.findall('\d{2}/\w{3}/\d{4}\:\d\d\:\d\d\:\d\d', line)[0]
             for line in open('/etc/httpd/logs/access_log')) # creating a list of all dates that found in the text
after_midnight = (((datetime.strptime(x, '%d/%b/%Y:%H:%M:%S') - midnight).days*24*3600+(datetime.strptime(x, '%d/%b/%Y:%H:%M:%S')- midnight).seconds) #converts string to date
                  #check that dates bigger than midnight
                  #put it in the list "after_midnight"
                  for x in time_stamp if datetime.strptime(x, '%d/%b/%Y:%H:%M:%S') >= midnight)
#created a list of 10 elements from "after_midnight" list and print it
for i in [next(after_midnight) for _ in range(10)]:
    print (i)
