using System;

namespace deckofcards
{
    public class Card{
        public string stringVal {
            get {
                if (val == 1){
                    return "A";
                }
                else if (val > 1 && val < 11){
                    return val.ToString();
                }
                else if (val == 11){
                    return "J";
                }
                else if (val == 12){
                    return "Q";
                }
                else if (val == 13){
                    return "K";
                }
                else{
                    return "not a card";
                }
            }
        }
        public string suit;
        public int val;
        public Card(string cardSuit, int num) {
            suit = cardSuit;
            val = num;
        }
    }
}
