import datetime
#clasinn Order car tekur inn afhendingardag, skiladag spyr notneda hvort hann vilji 
# aukatryggingu, reiknar svo út heildarverð og skilar því
class OrderCar:
  def __init__(self):
    self.__cars = ""

  def date_time_return(self):
    print("\tAfhendingardagur:")
    day, month, year = input("DD/MM/YYYY\n").split("/")
    day = int(day)
    month = int(month)
    year = int(year)
    today = datetime.date(year, month, day)
    print("\tSkiladagur: ")
    retday, retmonth, retyear = input("DD/MM/YYYY\n").split("/")
    retday = int(retday)
    retmonth = int(retmonth)
    retyear = int(retyear)
    someday = datetime.date(retyear, retmonth, retday)  
    return today,someday

  def order_price(self):
    today,someday = self.date_time_return()
    diff = someday - today  
    days = diff.days
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

    #def store_data(self, passport, fullprice, date1, date2)


    #þurfum að gera þetta fall á morgun sem geymir gögn
    #def store_order_data(self):





