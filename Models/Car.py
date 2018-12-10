class Car:

    def __init__(self, model, year, plate, miles, color, fuel_type, catagory, status):
        self.model = model
        self.year = year
        self.plate = plate
        self.miles = miles
        self.color = color
        self.fuel_type = fuel_type
        self.catagory = catagory
        self.status = status

    def __str__(self):
        return "{} {} {} {} {} {} {} {}".format(self.model, self.year, self.plate, self.miles, self.color, self.fuel_type, self.catagory, self.status)



