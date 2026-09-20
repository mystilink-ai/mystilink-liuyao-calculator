using System;
using Mystilink.Liuyao;

class Program
{
    static void Main()
    {
        string json = LiuyaoCalculator.Cast(seed: 123);
        Console.WriteLine(json);
    }
}
