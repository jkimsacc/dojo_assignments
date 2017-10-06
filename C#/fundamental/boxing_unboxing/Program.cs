using System;
using System.Collections.Generic;

namespace boxing_unboxing
{
    class Program
    {
        static void Main(string[] args)
        {
            List<object> stuff = new List<object>();
            stuff.Add(7);
            stuff.Add(28);
            stuff.Add(-1);
            stuff.Add(true);
            stuff.Add("chair");
            int sum = 0;
            foreach (object data in stuff){
                if (data is int){
                    sum += (int)data;
                }
                else if (data is string){
                    Console.WriteLine(data as string);
                }
            }
            Console.WriteLine(sum);
        }
    }
}
