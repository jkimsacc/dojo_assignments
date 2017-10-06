using System;

namespace humans{
    public class Human{
        public string name;
        public int strength { get; set; }
        public int intelligence { get; set; }
        public int dexterity { get; set; }
        public int health { get; set; }

        public Human(string input){
            name = input;
            health = 100;
            strength = 3;
            intelligence = 3;
            dexterity = 3;
        }
        public Human(string input, int str, int intel, int dex, int hp){
            name = input;
            strength = str;
            intelligence = intel;
            dexterity = dex;
            health = hp;
        }
        public void Attack(object human){
            Human target = human as Human;
            if(target != null){
                target.health -= 5*strength;
            }
            else{
                Console.WriteLine("Target not found");
            }
        }
    }

}