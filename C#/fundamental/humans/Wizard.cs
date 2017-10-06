using System;

namespace humans{
    public class Wizard : Human {
        public Wizard(string input) : base(input){
            health = 50;
            intelligence = 25;
        }
        public void Heal(){
            health += 10*intelligence;
            System.Console.WriteLine($"{name} gained {10*intelligence} health");
        }
        public void Fireball(object human){
            Human target = human as Human;
            if(target != null){
                Random rand = new Random();
                int dmg = rand.Next(20, 51);
                target.health -= dmg;
                System.Console.WriteLine($"{name} damaged {target.name} by {dmg} : {target.name} health: {target.health}");
            }
        }
    }
}