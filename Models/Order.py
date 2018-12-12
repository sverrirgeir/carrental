class Order:
    def __init__(self, passport, day1, day2, amount, carchoice, extraprice):
        self.passport = passport 
        self.pick_up_day = day1
        self.return_day = day2
        self.amount = amount
        self.type = carchoice
        self.extraprice = extraprice
        

    def __str__ (self):
        return "{} {} {} {} {}".format( self.passport, self.pick_up_day, self.return_day, self.amount, self.extraprice)

    def get_passport(self):
        return self.passport
    
    def get_pickup_day(self):
        return self.pick_up_day
    
    def get_return_day(self):
        return self.return_day
    
    def get_amount(self):
        return self.amount
    
    def get_type(self):
        return self.type
    
    def get_extraprice(self):
        return self.extraprice

    def get_write(self):
        return "{},{},{},{},{},{}".format(self.passport, self.pick_up_day, self.return_day, self.amount, self.type, self.extraprice)
    

