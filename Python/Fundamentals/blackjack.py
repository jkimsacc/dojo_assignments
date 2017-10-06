class Blackjack(object):
    def __init__(self, num_player, dealer = True):
        self.num_player = num_player
        self.dealer = dealer

    def setup(self, number_of_players, number_of_set):
        #create new deck
        #determine # of players
        pass
    def game(self):
        #hand card
        pass

    def hit(self):
        #add card to deck
        pass

    def stay(self):
        #end turn without getting a card
        #automatically pass next turn, until game ends
        #if both player stay, ends the game: calls evaluate function
        pass

    # def


def wincondition(result):
    #if dealer != 21 and player == 21
    #while dealer & player < 21, player < dealer
    #if player < 21 and dealer >21
    #else all lose
    print result
