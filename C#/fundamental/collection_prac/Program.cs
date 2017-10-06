using System;
using System.Collections.Generic;

namespace collection_prac
{
    class Program
    {
        static void Main(string[] args)
        {
            // Console.WriteLine("Hello World!");
            // // int[] arr = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
            // string[] names = {"Tim", "Martin", "Nikki", "Sara"};
            // bool[] boolarr = new bool[10];
            // for (int i = 0; i < 10; i++){
            //     if( i % 2 == 0){
            //         boolarr[i] = true;
            //         Console.WriteLine(boolarr[i]);
            //     }
            //     else{
            //         boolarr[i] = false;
            //         Console.WriteLine(boolarr[i]);
            //     }
            // }
            // int[] arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
            // int[,] multitable = new int[10, 10];
            // for (int f = 1; f < 11; f++){
            //     for (int idx = 0; idx < arr.Length; idx++){
            //         multitable[f-1, idx] = f*arr[idx];
            //         Console.Write(multitable[f-1,idx]);
            //         // multitable[f-1][idx] = arr[idx]*f; 
            //         // Console.Write("{0}, ", multitable[f][idx]);
            //     }
            // }
            List<string> flavors = new List<string>();
            flavors.Add("sour");
            flavors.Add("sweet");
            flavors.Add("salty");
            flavors.Add("Murican");
            flavors.Add("asian");

            Console.WriteLine(flavors.Count);


            Random flavor = new Random();
            string joseph = flavors[flavor.Next(1,flavors.Count)];
            string nick = flavors[flavor.Next(1,flavors.Count)];
            string jason = flavors[flavor.Next(1,flavors.Count)];
            string mars = flavors[flavor.Next(1,flavors.Count)];

            Dictionary<string, string> userInfo = new Dictionary<string, string>();
            userInfo.Add("Joseph",joseph);
            userInfo.Add("Nick",nick);
            userInfo.Add("Jason",jason);
            userInfo.Add("Mars",mars);

            foreach (KeyValuePair<string,string> entry in userInfo){
                Console.WriteLine(entry.Key + "-" + entry.Value);
            }
        }
    }
}
