#
# Example file for working with date information
# LinkedIn Learning Python course by Joe Marini
#

from datetime import date, time, datetime, timedelta

def main():
    ## DATE OBJECTS
    # TODO: Get today's date from the simple today() method from the date class
    today = date.today()
    print("today's date is", date.today())


    # TODO: print out the date's individual components
    print("Date Components:", today.day, today.month, today.year)
    
    # TODO: retrieve today's weekday (0=Monday, 6=Sunday)
    print("Today's Weekday #: ", today.weekday())
    days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    print("Which is a:", days[today.weekday()])
    
    ## DATETIME OBJECTS
    # TODO: Get today's date from the datetime class
    today = datetime.now()
    print("The current date and time is", today)
    
    # TODO: Get the current time
    t = datetime.time(datetime.now())
    print("the current time is:", t)

 

  
if __name__ == "__main__":
    main()
  