using System;
using System.Collections.Generic;
using System.Linq;

namespace deckofcards
{
    public class Deck{
        public List<Card> cards;

        public Deck(){
            Reset();
        }
        public Deck Reset(){
            cards = new List<Card>();
            string[] suits = new string[4] {"H", "C", "S", "D"};
            foreach(string suit in suits){
                for(int val = 1; val < 14; val++) {
                    cards.Add(new Card(suit, val));
                }
            }
            Shuffle();
            return this;
        }
        public Card Deal(){
            if(cards.Count == 0){
                Reset();
            }
            Card draw = cards[0];
            cards.Remove(cards[0]);
            return draw;
        }
        public Deck Shuffle(){
            Random rand = new Random();
            for (int idx = cards.Count-1; idx > 0; idx--){
                int randIdx = rand.Next(0, idx);
                Card temp = cards[randIdx];
                cards[randIdx] = cards[idx]; 
                cards[idx] = temp;
            }
            return this;
        }
    }
}
