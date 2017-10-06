# helper Function that look through compatible list,
# if new key does not exist add its key

def update_list(name, somedic):
    for key in somedic:
        if key == name:
            return False
        else:
            return True


class Smarthome(object):
    """docstring forSmarthome."""
    def __init__(self, name, brand, price, type, compatible ={}):
        self.name = name
        self.brand = brand
        self.price = price
        self.type = type
        self.compatible = compatible

    def display_price(self):
        print "price: $", self.price
        return self

    def display_compatible(self):
        update_list(self.name, self.compatible)
        print "compatible list", self.compatible
        return self


samsung_smartthings = Smarthome("Smartthings", "Samsung", 199, "Hub")
Alexa_echo = Smarthome("Alexa Echo", "Amazon", 20, "Voicd hub", {"Smartthings"})

samsung_smartthings.display_price().display_compatible()
