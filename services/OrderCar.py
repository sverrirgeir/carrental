import datetime

class OrderCar:
  pass 
def date_time_return():
  today = datetime.date.today()
  ar = int(input("Ár: "))
  manudur = int(input("Manudur: "))
  dagur = int(input("Dagur: "))
  someday = datetime.date(ar, manudur, dagur)
  diff = someday - today
  print(diff.days)
        
  return diff.days

    

allt = date_time_return()
print(allt)






