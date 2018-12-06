import datetime

class OrderCar:
  pass 
def date_time_day():
    day = datetime.date.today().strftime("%d")
    return day 
def date_time_month():
    month = datetime.date.today().strftime("%m")
    return month
def date_time_return():
    monthr = int(input("Mánuður: "))
    dayr = int(input("Day: "))
    month = date_time_month()
    day = date_time_day()
    alldays = int(day) - dayr
    return alldays

    

allt = date_time_return()
print(allt)






