import random

def createcards(self):

    for val in self.vals:
        for color in range(len(self.colors)):
            #print  str(self.vals[val-2]), self.colors[color]
            lol = str(self.vals[val-2]) + self.colors[color]
            self.cards.append(lol)
    #print self.cards

def shuffle(self):
    random.shuffle(self.cards)
    print self.cards

def initialdraw(self):
    self.playerhand = []
    self.computerhand =[]
    for i in range (0, 4):
        if i % 2 == 0:
            self.playerhand.append(self.cards[len(self.cards)-1])
            self.cards.pop(self.cards[len(self.cards)-1])
            print "player got a card"
            # print playerhand
        else:
            self.computerhand.append(self.cards[len(self.cards)-1])
            self.cards.pop(self.cards[len(self.cards)-1])
            print "computer got a card"
            # print computerhand
    print self.playerhand, self.computerhand
    return self.playerhand, self.computerhand
def start(self):
    return initialdraw()


def convertcard2num(string):
    if string[0] == "A":
        string = 11
    # print string
    return string
elif string[0] == "J" or string[0] == "Q" or string[0] == "K" or string[0] == "1":
    string = 10
    # print string
    return string
else:
    string = int(string[0])
    # print string
    return string

# game = twentyone()
# game.createcards()
# game.shuffle()
#twentyone().createcards().shuffle().initialdraw()

def wincondition()
