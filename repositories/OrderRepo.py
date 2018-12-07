from Models.Order import Order

class OrderRepo:
    def __init__(self):
        pass

    def write_car_order(self, order):
        order_string = order.get_write()
        with open("./data/orders.txt", "a") as orderfile:
            orderfile.write(order_string)
            orderfile.write("\n")