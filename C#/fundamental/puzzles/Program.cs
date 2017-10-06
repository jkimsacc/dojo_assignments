using System;
using System.Collections.Generic;

namespace puzzles
{
    class Program
    {
        
        public static int[] RandomArray(){
            int[] randomArray = new int[10];
            Random rand = new Random();
            for (int i = 0; i < randomArray.Length; i++){
                randomArray[i] = rand.Next(5, 25);
            };
            int min = randomArray[0];
            int max = randomArray[0];
            foreach(int val in randomArray){
                Console.WriteLine(val);
                if (val < min) {
                    min = val;
                }
                if (val > max) {
                    max = val;
                }
            }
            Console.WriteLine($"Max is {max}, min is {min}");
            return randomArray;
        }

        

        public static string TossCoin(){
            Random rand = new Random();
            int toss = rand.Next(0,2);
            string coin = null;
            if ( toss == 0){
                coin = "Heads";
            }
            else if ( toss == 1){
                coin = "Tails";
            }
            // Console.WriteLine("Tossing a Coin!");
            // Console.WriteLine(coin);
            return coin;
        }
        public static double TossMultipleCoins(int num){
            double heads = 0;
            for (int i = 0; i < num; i++){
                TossCoin();
                if(TossCoin()=="Heads"){
                    heads += 1;
                }
            }
            Console.WriteLine(heads/num);
            return heads/num;
        } 

        public static string[] Names(){
            string[] names = new string[5];
            names[0]="Todd";
            names[1]="BoJack";
            names[2]="Diane";
            names[3]="Mr.P";            
            names[4]="Princess C";
            Random rand = new Random();
            for ( int i = names.Length -1 ; i > 0; i --){
                string temp = names[i];
                int randIdx = rand.Next(0, i);
                names[i] = names[randIdx];
                names[randIdx] = temp;
            }
            List<string> nameslist = new List<string>();
            foreach( string name in names){
                int nameLength = name.Length;
                if ( nameLength > 5){
                    Console.WriteLine(name+" added");
                    nameslist.Add(name);
                }
            }
            return nameslist.ToArray();
        }

        static void Main(string[] args)
        {
            // RandomArray();
            // TossCoin();
            // TossMultipleCoins(1_000_000_000);
            Names();
        }
        
    }
}
