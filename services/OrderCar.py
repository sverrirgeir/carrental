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
    '''Fallið tekur inn input DD/MM/YYYY og skilar síðan út í mismunandi breytum'''
    day, month, year = input("\n\tAfhendingardagur(DD/MM/YYYY): ").split("/")
    day = int(day)
    month = int(month)
    year = int(year)
    '''Hérna formata ég yfir í datetime formið til að geta borið saman föllin'''
    today = datetime.date(year, month, day)
    ret_day, ret_month, ret_year = input("\tSkiladagur(DD/MM/YYYY): ").split("/")
    ret_day = int(ret_day)
    ret_month = int(ret_month)
    ret_year = int(ret_year)
    '''Við tökum baða dagana núna og berum þá saman til að geta séð hver mismunur dagana er mikill til að reikna út verð'''
    someday = datetime.date(ret_year, ret_month, ret_day) 
    return today,someday

  def order_price(self):
    today,someday = self.date_time_return()
    diff = someday - today  
    days = diff.days
    days = days + 1
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
    insurance = input("\n\tAukatryggingu?(y/n): ")
    ''' hér breyti ég inputinu í lower til að engin misskilningur verði á'''
    extraprice = 0
  
    if insurance.lower() == "y":
      extraprice = 30000
    return price,today,someday,carchoice,extraprice
  
  def get_car_order(self, order):
    return self.__write_order.write_car_order(order)
  

  def print_list_of_orders(self):
    return self.__write_order.print_orders()

  def search_for_orders(self, passport):
    """tekur inn vegabréfsnr og villutjekkar áður en hann sendir það í repo"""
    if self.validate_passport(passport):
      return self.__write_order.search_for_orders(passport)

  def validate_passport(self, passport):
    if len(passport) == 8:
      return True
    else:
      return False

  def delete_order(self, number):
    return self.__write_order.delete_order(number)

  def get_order(self, number):
    return self.__write_order.get_order(number)

  



