import datetime

class OrderCar:
  def __init__(self):
    self.__cars = ""

  def date_time_return(self):
    today = datetime.date.today()
    print("\tSkiladagur:")
    year = int(input("\tÁr: "))
    month = int(input("\tMánuður: "))
    day = int(input("\tDagur: "))
    someday = datetime.date(year, month, day)
    diff = someday - today    
    return diff.days

  def order_price(self):
    days = self.date_time_return()
    print("\tVeldu tegund: \n\t1. Smábíll \n\t2. Fólksbíll \n\t3. jeppi \n\t4. Húsbíll " )
    carchoice = int(input("\tVal: "))
    price = 0
    if carchoice == 1:
      price = days * 10000
    elif carchoice == 2:
      price = days * 15000
    elif carchoice == 3:
      price = days * 20000
    elif carchoice == 4:
      price = days * 25000
    else:
      print("Ekkert valið")  
      self.order_price()
    insurance = input("\tAukatryggingu?(y/n): ")
    if insurance == "y":
      fullprice = price + 30000
    else:
      fullprice = price
    return fullprice

    #þurfum að gera þetta fall á morgun sem geymir gögn
    #def store_order_data(self):





