import random
class twentyone(object):
    def init(self):
        J = 10
        Q = 10
        K = 10
        A = 11
        self.vals = [2, 3, 4, 5, 6, 7, 8, 9, 10]#, J, Q, K, A]
        self.cards = []
        self.colors = ["H", "D", "P", "C"]
        self.playerhand = []
        self.computerhand = []
        self.sump = 0
        self.sumc = 0
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
    for i in range (0, 4):
        if i % 2 == 0:
            self.playerhand.append(self.cards[len(self.cards)-1])
            #print self.cards[len(self.cards)-1]
            self.cards.pop(len(self.cards)-1)
            print "player got a card"
            # print playerhand
        else:
            self.computerhand.append(self.cards[len(self.cards)-1])
            self.cards.pop(len(self.cards)-1)
            print "computer got a card"

            # print computerhand
    print "Your cards", self.playerhand
    print "Dealer's cards", self.computerhand
    print len(self.playerhand[1])
    print len(self.playerhand[0])
    print "*********"
    if len(self.playerhand[0]) ==2:
        self.sump += int(self.playerhand[0][0])
    else:
        self.sump += int(self.playerhand[0][0])+int(self.playerhand[0][1])
    if len(self.playerhand[1]) ==2:
        self.sump += int(self.playerhand[1][0])
    else:
        self.sump += int(self.playerhand[1][0])+int(self.playerhand[1][1])



    self.sumc = int(self.computerhand[1][0]) + int(self.computerhand[0][0])
    print self.sump
    print self.sumc
    print "FIGURE OUT WHO WON!"
    return self.playerhand, self.computerhand

def convertplayer(self, cards):
    #fisrt card
    if self.cards[0][0] == "A":
        self.sump += 10
    elif self.cards[0][0] == "J" or self.cards[0][0] == "Q" or self.cards[0][0] == "K" or self.cards[0][0] == "1":
        self.sump += 10
        return string
    else:
        self.sump += int(self.cards[0][0])

    if self.cards[1][0] == "A":
        self.sump += 10
    elif self.cards[1][0] == "J" or self.cards[1][0] == "Q" or self.cards[1][0] == "K" or self.cards[1][0] == "1":
        self.sump += 10
        return string
    else:
        self.sump += int(self.cards[1][0])

def convertcomputer():
    #fisrt card
    if self.cards[0][0] == "A":
        self.sump += 10
    elif self.cards[0][0] == "J" or self.cards[0][0] == "Q" or self.cards[0][0] == "K" or self.cards[0][0] == "1":
        self.sump += 10
        #print string
        return string
    else:
        self.sump += int(self.cards[0][0])

    if self.cards[1][0] == "A":
        self.sump += 10
    elif self.cards[1][0] == "J" or self.cards[1][0] == "Q" or self.cards[1][0] == "K" or self.cards[1][0] == "1":
        self.sump += 10
        # print string
        return string
    else:
        self.sump += int(self.cards[1][0])





def sum(self):
    print "hey"
    #for i in self.playerhand:

        #print self.sump
        #return sum
def start(self):
    return initialdraw()
game = twentyone()
game.createcards()
game.shuffle()
game.shuffle()
game.initialdraw()
#game.sum()
#twentyone().createcards().shuffle().initialdraw()
