class Animal(object):
    # """docstring for Animal."""
    def __init__(self, name):
        # super(Animal, self).__init__()
        self.name = name
        self.health = 100

    def walk(self):
        print "walking"
        self.health -= 1
        if self.health <= 0:
            print self.name, "dieded"
        return self

    def run(self):
        print "runiing"
        self.health -= 5
        if self.health <= 0:
            print self.name, "dieded"
        return self

    def display(self):
        print self.name
        print self.health

Shiba = Animal("doge")
Shiba.walk().walk().walk().run().run().display()

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        self.health += 5

husky = Dog('moonmoon')
husky.display()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170

    def fly(self):
        self.health -= 10

    def display(self):
        print "I am a Dragon"
        super(Dragon, self).display()





Charizard = Dragon("I am not a dragon")
Charizard.fly()
Charizard.display()
