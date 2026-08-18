
using System;
using System.Reflection;

class Program
{
    static void Main()
    {
        try
        {
            var gameRes = Assembly.LoadFrom("GameRes.dll");
            var arcFormats = Assembly.LoadFrom("ArcFormats.dll");
            
            Console.WriteLine("Searching in GameRes.dll:");
            foreach (var t in gameRes.GetTypes())
            {
                if (t.Name.Contains("Callback"))
                    Console.WriteLine("  " + t.FullName);
            }
            
            Console.WriteLine("Searching in ArcFormats.dll:");
            foreach (var t in arcFormats.GetTypes())
            {
                if (t.Name.Contains("Callback"))
                    Console.WriteLine("  " + t.FullName);
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine("Error: " + ex);
        }
    }
}
