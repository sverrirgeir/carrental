from Models.Order import Order

class OrderRepo:
    def __init__(self):
        pass

    def write_car_order(self, order):
        order_string = order.get_write()
        with open("./data/orders.txt", "a") as orderfile:
            orderfile.write(order_string)
            orderfile.write("\n")
    
    def print_orders(self):
        with open("./data/orders.txt", "r") as ordersf:
            print("\n\t{:<10}\t{:^10}\t{:^10}\t{:^10}\t{:^10}".format("Vegabréfa N.","Afhendingard.","Skilad.","Verð","Flokkur"))
            print(" "*8 + "-"*72)
            for line in ordersf:
                linesplit = line.split(",")
                passport = linesplit[0]
                pickupdate = linesplit[1]
                returndate = linesplit[2]
                price = linesplit[3]
                price = int(price)
                price = "{:,}".format(price)
                price = str(price) + " kr"
                tegund = linesplit[4]
                if tegund == "1":
                    tegund = "Smábíll"
                elif tegund == "2":
                    tegund = "Fólksbíll"
                elif tegund == "3":
                    tegund = "Jeppi"
                else:
                    tegund = "Húsbíll"
                print("\n\t{:<10}\t{:^10}\t{:^10}\t{:^10}\t{:^10}".format(passport, pickupdate, returndate, price, tegund))

            return