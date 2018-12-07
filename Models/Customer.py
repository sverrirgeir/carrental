class Customer:

    def __init__(self, first_name, last_name, passport, kredit, middle_name = ""):
        self.fullname = first_name + " " + middle_name + " " + last_name
        self.passport = passport
        self.kredit = kredit

    def __str__(self):
        return "{} {}".format(self.fullname, self.passport)

    def get_kredit(self):
        return self.kredit
    
    def get_passport(self):
        return self.passport
        
    def get_write(self):
        return "{},{},{}".format(self.fullname, self.passport, self.kredit)