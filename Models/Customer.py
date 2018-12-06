class Customer:

    def __init__(self, name, passport, kredit):
        self.name = name
        self.passport = passport
        self.kredit = kredit

    def __str__(self):
        return "{} {}".format(self.name, self.passport)
