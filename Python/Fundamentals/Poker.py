import random

#create class of game
#create deck
#shuffle
# start function initial draw = hand in 2 cards each
# calculate value in card
# decide to draw or not -computer = if second card is less than 5 draw extra
#   play draw if raw_input == draw
# examine result


def createDeck():
    deck = []
    shape = ["D", "C", "H", "S"]
    number = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    for i in range(0, len(shape)-1):
        for j in range(0, len(number)-1):
            card = shape[i] + number[j]
            deck.append(card)
    random.shuffle(deck)
    # print deck, "deck created"
    return deck

def calcsum(cardlist):
    score = 0
    for i in range(0, len(cardlist)):
        if cardlist[i][1] == "A":
            score += 11
        elif cardlist[i][1] == "J" or cardlist[i][1] == "Q" or cardlist[i][1] == "K" or cardlist[i][1] == "1":
            score += 10
        else:
            score += int(cardlist[i][1])
            # print int(cardlist[i][1])
    return score

class Blackjack(object):
    def __init__(self):
        self.deck = []
        self.player_hand = []
        self.computer_hand = []

    def start(self):
        self.deck = createDeck()
        # print self.deck
        self.playerhand = []
        self.computerhand =[]
        for i in range (0, 4):
            if i % 2 == 0:
                self.playerhand.append(self.deck[len(self.deck)-1])
                self.deck.pop(len(self.deck)-1)
                # return self.playerhand
            else:
                self.computerhand.append(self.deck[len(self.deck)-1])
                self.deck.pop(len(self.deck)-1)
        print "player:", self.playerhand, "-", calcsum(self.playerhand)
        print "computer:", self.computerhand, "-", calcsum(self.computerhand)
        return self

    def draw(self):
        for i in range (0, 2):
            if i == 0:
                self.playerhand.append(self.deck[len(self.deck)-1])
                self.deck.pop(len(self.deck)-1)
                print "player:", self.playerhand, "-", calcsum(self.playerhand)
            else:
                if calcsum(self.computerhand) < 14:
                    self.computerhand.append(self.deck[len(self.deck)-1])
                    self.deck.pop(len(self.deck)-1)
                    print "computer:", self.computerhand, "-", calcsum(self.computerhand)
                else:
                    print "computer:", self.computerhand, "-", calcsum(self.computerhand)
        return self

    def end(self):
        if calcsum(self.playerhand) == 21 and calcsum(self.computerhand) != 21:
            print "Player WON"
        elif calcsum(self.playerhand) != 21 and calcsum(self.computerhand) == 21:
            print "Computer WON"
        elif calcsum(self.playerhand) > 21 and calcsum(self.computerhand) < 21:
            print "Computer WON"
        elif calcsum(self.playerhand) < 21 and calcsum(self.computerhand) > 21:
            print "Player WON"
        elif calcsum(self.playerhand) < 21 and calcsum(self.computerhand) < 21:
            if calcsum(self.playerhand) > calcsum(self.computerhand):
                print "Player Won"
            elif calcsum(self.playerhand) < calcsum(self.computerhand):
                print "Computer Won"
        else:
            print "NO ONE WINS"
        return self







game1 = Blackjack()
game1.start().draw().end().fdfd
