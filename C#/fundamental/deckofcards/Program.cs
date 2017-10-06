using System;

namespace deckofcards
{
    class Program
    {
        static void Main(string[] args)
        {
            Deck newDeck = new Deck();
            Player joseph = new Player("Joseph");
            joseph.DrawCard(newDeck);
            joseph.DrawCard(newDeck);
            Console.WriteLine(joseph.hand[0].val);
        }
    }
}
