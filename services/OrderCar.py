import datetime

class OrderCar:
  def __init__(self):
    self.__cars = ""

  def date_time_return(self):
    today = datetime.date.today()
    ar = int(input("Ár: "))
    manudur = int(input("Manudur: "))
    dagur = int(input("Dagur: "))
    someday = datetime.date(ar, manudur, dagur)
    diff = someday - today    
    return diff.days

  def order_price():
    days = date_time_return(self)
    print("Veldu tegund: \n1. Smábíll \n2. Fólksbíll \n3. jeppi \n4. Húsbíll " )
    carchoice = int(input())
    price = 0
    if carchoice == 1:
      price = days * 10000
      print(price)
    elif carchoice == 2:
      price = days * 15000
      print(price)
    elif carchoice == 3:
      price = days * 20000
      print(price)
    elif carchoice == 4:
      price = days * 25000
      print(price)
    else:
      print("Ekkert valið")  
      order_price()
    incurance = input("Viltu Aukatryggingu? y/n: ")
    if incurance == "y":
      fullprice = price + 30000
    else:
      fullprice = price
    return fullprice
  


    


order_price()





