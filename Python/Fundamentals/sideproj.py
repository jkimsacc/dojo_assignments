class IoT(object):
    """docstring forIoT."""
    def __init__(self, name, brand, compatible_with=[]):
        self.name = name
        self.brand = brand
        self.compatible_with = compatible_with


Samsung = IoT("Smartthings", "Samsung", [])
Alexa = IoT("Alexa Echo", "Amazon", ["Samsung"])
print Samsung.name
print Samsung.brand
print Samsung.compatible_with
print Alexa.name
print Alexa.brand
print Alexa.compatible_with
