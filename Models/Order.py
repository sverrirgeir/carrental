class Order:
    def __init__(self, passport, day1, day2, amount):
        self.passport = passport 
        self.pick_up_day = day1
        self.return_day = day2
        self.amount = amount

    def __str__ (self):
        return "{} {} {} {}".format( self.passport, self.pick_up_day, self.return_day, self.amount)

    def get_passport(self):
        return self.passport
    
    def get_pickup_day(self):
        return self.pick_up_day
    
    def get_return_day(self):
        return self.return_day
    
    def get_amount(self):
        return self.amount
    

