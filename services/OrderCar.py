import datetime
from Models.Order import Order
from repositories.OrderRepo import OrderRepo
#clasinn Order car tekur inn afhendingardag, skiladag spyr notneda hvort hann vilji 
# aukatryggingu, reiknar svo út heildarverð og skilar því
class OrderCar:
  def __init__(self):
    self.__cars = ""
    self.__write_order = OrderRepo()

  def date_time_return(self):
    day, month, year = input("\n\tAfhendingardagur(DD/MM/YYYY): ").split("/")
    day = int(day)
    month = int(month)
    year = int(year)
    today = datetime.date(year, month, day)
    ret_day, ret_month, ret_year = input("\tSkiladagur(DD/MM/YYYY): ").split("/")
    ret_day = int(ret_day)
    ret_month = int(ret_month)
    ret_year = int(ret_year)
    someday = datetime.date(ret_year, ret_month, ret_day) 
    return today,someday

  def order_price(self):
    today,someday = self.date_time_return()
    diff = someday - today  
    days = diff.days
    print("\n\tVeldu tegund: \n\n\t\t1. Smábíll \n\t\t2. Fólksbíll \n\t\t3. jeppi \n\t\t4. Húsbíll " )
    carchoice = int(input("\n\t\tVal: "))
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
    return fullprice,today,someday,carchoice
  
  def get_car_order(self, order):
    return self.__write_order.write_car_order(order)
    


    #def store_data(self, passport, fullprice, date1, date2)


    #þurfum að gera þetta fall á morgun sem geymir gögn
    #def store_order_data(self):





