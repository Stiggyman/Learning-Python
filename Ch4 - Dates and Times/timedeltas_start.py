#
# Example file for working with timedelta objects
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date, time, datetime, timedelta


# TODO: construct a basic timedelta and print it
print(timedelta(days=365, hours=5, minutes=1))

# TODO: print today's date
now = datetime.now()
print("today is: " + str(now))

# TODO: print today's date one year from now
print("one year from now it will be: " + str(now + timedelta(days=365)))

# TODO: create a timedelta that uses more than one argument
print("in 2 weeks and 3 days it will be", str(now + timedelta(weeks=2, days=3)))

# TODO: calculate the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print("one week ago it was ", s)

### How many days until April Fools' Day?
todays_date = date.today()
afd = date(todays_date.year, 4, 1)


# TODO: use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if afd < todays_date:
    print("April Fool's day already went by %d days ago" % ((todays_date-afd).days))
    afd = afd.replace(year=todays_date.year+1)

# TODO: Now calculate the amount of time until April Fool's Day  
time_to_afd = afd - todays_date
print("it is" ,time_to_afd.days, "days until next april fools day")
