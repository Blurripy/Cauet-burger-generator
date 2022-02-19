using System;
using System.Threading;

namespace CauetBurgerGenerator
{
  class Program
  {
    static void Main(string[] args)
    {
      string[] ingredients = new string[] { "pain du dessus", "sauce", "tomtates", "fromage", "steaks", "sauce", "salade", "pain du dessous"};

      for ( int i = 0; i != ingredients.Length; i++) {
        Console.Write(ingredients[i] + " : ");
        Thread.Sleep(2000);
        Console.WriteLine("terminé");
      }
    }
  }
}
