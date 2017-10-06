using System;

namespace humans{
    public class Ninja : Human {
        public Ninja(string input) : base(input){
            dexterity = 175;
        }
        public void StealLife(object human){
            Human target = human as Human;
            Random rand = new Random();
            if (rand.Next(0,2) == 1){
                target.health -= 75;
                health = 75;
                System.Console.WriteLine($"Critical! {target.name} lost 75, {name} gained 75 health." );
            }
            else{
                target.health -= 10;
                health += 10;
                System.Console.WriteLine($"Failed.. {target.name} lost 10, {name} gained 10 health.");
            }
        }
        public void GetAway(){
            health += 15;
            System.Console.WriteLine($"{name} got away successfully.");
        } 
    }
}