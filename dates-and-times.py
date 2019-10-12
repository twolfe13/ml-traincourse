import datetime 



def time(): 
    #define start time and end time
    start_time = datetime.time(7,0)
    print(start_time)
    
    end_time = datetime.time(9,0)
    print(end_time)
    
    #define start date and end date 
    start_date = datetime.date(2016,5,1)
    print(start_date)
    
    end_date = datetime.date(2016,6,2)
    print(end_date)
    
    start_datetime = datetime.datetime.combine(start_date,start_time)
    print(start_datetime)
    
    end_datetime = datetime.datetime.combine(end_date, end_time)
    print(end_datetime)
    
    
    
    # timedeltas
#Differences between datetimes are timedelta objects

    timedelta_total = end_datetime - start_datetime
    print(timedelta_total)
# timedeltas have 3 values.. days, seconds, and microseconds
# They can be used to increment dates and times, accounting for quirks in 
#dates and timezones 

    end_datetime = start_datetime + timedelta_total
    print(end_datetime)
    
#    unix_epoch = datetime.timestamp(start_datetime)
#   start_datetime = datetime.datetime.fromtimestamp(1457453760)
#   print(unix_epoch)
    
    #Current date and time 
    now = datetime.datetime.now()
    print("the current time is:")
    print(now)
    
#Weekday - Gets the da of the week for a given date 
# Monday is 0, Sunday is 6

    weekday_number = start_datetime.date().weekday()
    print(weekday_number)
    
    if weekday_number is 6: 
        print("The day is Saturday!")
        
        
#Converting a date to and from a string - useful for taking in text from a text
# file, and/or want to turn text dates into datetime objects. It's also helpful
# if we want to expose our datetime object to a user, or export it to a txt file

 # Pass a date string and a code for interpreting it (required)
  # in this snippet, %Y = year; %m = month; %d = day
  
 # int'l standard for represnting dates is in this way

    new_datetime = datetime.datetime.strptime('2018-06-21', '%Y-%m-%d')
    print(new_datetime)

  # Turn the datetime into a date string
    
    datestr = new_datetime.strftime('%Y-%m-%d')
    print(datestr)
    print(datestr + " " + "this is a great date!")


# Call the function    
time()
