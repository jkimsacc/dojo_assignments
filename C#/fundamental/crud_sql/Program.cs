using System;
using System.Collections.Generic;
using System.Linq;
using DbConnection;

namespace DbConnection
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
        }
        public void Read(){
            List<Dictionary<string, object>> allUsers = DbConnector.Query("SELECT * FROM users");
            foreach(Dictionary<string, object> user in allUsers){
                System.Console.WriteLine(user);
            }
        }
        public void Create(){
            System.Console.WriteLine("input first name");
            string firstname = Console.ReadLine();
            DbConnector.Execute($"INSERT INTO users FirstName VALUES {firstname}");
            System.Console.WriteLine("input last name");
            string lastname = Console.ReadLine();
            DbConnector.Execute($"INSERT INTO users LastName VALUES {lastname}");
            System.Console.WriteLine("input your favorite number");
            string favorite = Console.ReadLine();
            int favoritenum;
            bool result = Int32.TryParse(favorite, out favoritenum);
            DbConnector.Execute($"INSERT INTO users FavoriteNum VALUES {favoritenum}");
        }    
    }

}
