class car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
    def display_all(self):
        print self.price
        print self.speed
        print self.fuel
        print self.mileage
        if self.price >= 10000:
            print "15%"
        else:
            print "12%"

bmw = car(40000, 260, "full", 400)
bmw.display_all()
