using System;
using System.Collections.Generic;
using System.Linq;

namespace deckofcards
{
    public class Player{
        public string name;
        public List<Card> hand;

        public Player(string player_name) {
            hand = new List<Card>();
            name = player_name;
        }
        public Card DrawCard(Deck currentDeck){
            hand.Add(currentDeck.Deal());
            return currentDeck.Deal();
        }
        public Card Discard(int index){
            if (hand.Count > 0){
                Card temp=hand[index];
                hand.Remove(hand[index]);
                return temp;
            }
            else{
                return null;
            }
        }
    }       
}
