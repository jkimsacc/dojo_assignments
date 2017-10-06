using System;

namespace humans{
    public class Samurai : Human {
        public Samurai(string input) : base(input){
            health = 200;
        }
        public void DeathBlow(object human){
            Human target = human as Human;
            if (target.health < 50){
                target.health = 0;
                System.Console.WriteLine($"Death Blow! {target.name} died.");
            }
            else{
                Console.WriteLine("Nothing Happend");
            }
        }
        public void Meditate(){
            health = 200;
            System.Console.WriteLine($"Meditate! {name} gained full health.");
        } 
    }
}