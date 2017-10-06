using System;
using System.Collections.Generic;
using System.Linq;
using JsonData;

namespace ConsoleApplication
{
    public class Program
    {
        public static void Main(string[] args)
        {
            //Collections to work with
            List<Artist> Artists = JsonToFile<Artist>.ReadJson();
            List<Group> Groups = JsonToFile<Group>.ReadJson();

            //There is only one artist in this collection from Mount Vernon, what is their name and age?
            IEnumerable<Artist> FromMtVernon = Artists.Where( h => h.Hometown == "Mount Vernon");
            foreach (Artist artist in FromMtVernon){
                System.Console.WriteLine($"Name: {artist.RealName}\nAge: {artist.Age}");
            }
            //Who is the youngest artist in our collection of artists?
            List<Artist> OrderedByAge = Artists.OrderBy(a => a.Age).ToList();
            System.Console.WriteLine($"{OrderedByAge[0].ArtistName} Age: {OrderedByAge[0].Age}");
            //Display all artists with 'William' somewhere in their real name
            IEnumerable<Artist> Williams = Artists.Where(a => a.RealName.Contains("William"));
            foreach (Artist artist in Williams){
                System.Console.WriteLine($"{artist.RealName}");
            }

            //Display the 3 oldest artist from Atlanta
            IEnumerable<Artist> OldiesFromAtlanta = Artists.Where(a => a.Hometown == "Atlanta").OrderByDescending(a => a.Age).Take(3);
            foreach(Artist artist in OldiesFromAtlanta){
                System.Console.WriteLine($"{artist.ArtistName}, {artist.Age} year-old, from {artist.Hometown}");
            }
            //(Optional) Display the Group Name of all groups that have members that are not from New York City

            IEnumerable<Artist> notNYartist = Artists.Where(a => a.Hometown != "New York City");
            IEnumerable<Group> notNYgroup = Groups.Join(notNYartist,
                                            g => g.Id,
                                            a => a.GroupId,
                                            (g, a) => {
                                                return g;
                                            }).Distinct();
            foreach(Group group in notNYgroup){
                System.Console.WriteLine($"{group.GroupName}");
            }
            //(Optional) Display the artist names of all members of the group 'Wu-Tang Clan'
            IEnumerable<Artist> wutang = Artists.Where(a => a.GroupId == Groups.Where(g => g.GroupName == "Wu-Tang Clan").First().Id);
            foreach(Artist artist in wutang){
                System.Console.WriteLine($"{artist.ArtistName}");
            }
        }
    }
}
