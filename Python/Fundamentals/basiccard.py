import random

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
    print deck
    return deck



# def han:
#     for i in range(1, num_player):
#         if dealer == num_card % num_player == 0:
#             dealer.append(deck(len(deck)-1))
#             print dealer
#         elif num_card % num_player == i:
#             player[i].append(deck(len(deck)-1))
#             pop.deck(len(deck)-1)
    # print dealer
    # print player[1]

# createDeck()
numofplayer(4)
handout(5, 5, createDeck())
