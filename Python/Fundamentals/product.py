class product(object):
    def __init__(self, price, item_name, weight, brand, cost, status):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "For sale"
    def sell(self):
        self.status = "Sold"
    def add_tax(self):
        self.tax = self.price * 0.1
        self.price += self.tax
    def return1(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        if reason == "in box":
            self.status = "For sale"
            self.price = self.price * 0.8
    def display(self):
        print "$", self.price
        print self.item_name
        print self.weight, "lb"
        print self.brand
        print self.status

macbook = product(1300, "Macbook", 1.2, "apple", 1200, "For sale")
macbook.display()
