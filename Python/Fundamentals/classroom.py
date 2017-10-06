class Classroom(object):
    def __init__(self, name):
        self.name = name
        self.kids = []

    def addkids(self, kid):
        self.kids.append(kid)
        print "kid added"
        return self

    def allspeak(self):
        for key in self.kids:
            key.speak()
            return self

class Kid(object):
    def __init__(self, firstnm, lastnm):    
        self.firstnm = firstnm
        self.lastnm = lastnm
    def speak (self):
        print "My name is {} {}".format(self.firstnm, self.lastnm)
        return self




loathesomeTyke1 = Kid("Joffrey", "Barratheon/Lannister")
loathesomeTyke2 = Kid("Viserys", "Targaryen")
loathesomeTyke3 = Kid("Ramsey", "Snow")
loathesomeTyke4 = Kid("Robin", "Arryn")
loathesomeTyke1.speak()

pythonclass = Classroom('python')
pythonclass.addkids(loathesomeTyke1)
pythonclass.allspeak()
