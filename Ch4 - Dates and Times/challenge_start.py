# Start file for programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
#

import calendar
from datetime import datetime, timedelta



exit = False
day_map = {1:calendar.MONDAY, 2:calendar.TUESDAY, 3:calendar.WEDNESDAY, 4:calendar.THURSDAY, 5:calendar.FRIDAY, 6:calendar.SATURDAY, 7:calendar.SUNDAY}
while not exit:
    print("Which day of the wekk do you want to count?")
    print("1. Monday")
    print("2. Tuesday")
    print("3. Wednesday")
    print("4. Thursday")
    print("5. Friday")
    print("6. Saturday")
    print("7. Sunday")
    print("8. Exit")
    choice = int(input("Enter your choice: "))
    
    if (choice == 8):
        exit = True
    else:
        print("what year do you want to count in?")
        year = int(input("Enter the year: "))
        print("what month do you want to count in?")
        month = int(input("Enter the month: "))

        cal = calendar.monthcalendar(year, month)


        count = 0
        weekone = cal[0]
        weektwo = cal[1]
        weekthree = cal[2]
        weekfour = cal[3]
        weekfive = cal[4]
        if weekone[day_map[choice]] != 0:
            count += 1
        if weektwo[day_map[choice]] != 0:
            count += 1
        if weekthree[day_map[choice]] != 0:
            count += 1
        if weekfour[day_map[choice]] != 0:
            count += 1
        if weekfive[day_map[choice]] != 0:
            count += 1
        print("There are", count, "of", calendar.day_name[day_map[choice]], "in", calendar.month_name[month], year)
        
        

# print("Team meetings will be on: ")
# for m in range(1,13):
#     cal = calendar.monthcalendar(2022, m)
#     weekone = cal[0]
#     weektwo = cal[1]

#     if weekone[calendar.FRIDAY] != 0:
#         meetday = weekone[calendar.FRIDAY]
#     else:
#         meetday = weektwo[calendar.FRIDAY]
    
#     print("%10s %2d" % (calendar.month_name[m], meetday))
    

        