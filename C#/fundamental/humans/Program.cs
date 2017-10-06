using System;

namespace humans
{
    class Program
    {
        static void Main(string[] args)
        {
            Wizard nick = new Wizard("Nick");
            Ninja joseph = new Ninja("Joseph");
            Samurai mars = new Samurai("Mars");
            nick.Fireball(joseph);
            joseph.StealLife(mars);
            joseph.GetAway();
            mars.DeathBlow(nick);
        }
    }
}
