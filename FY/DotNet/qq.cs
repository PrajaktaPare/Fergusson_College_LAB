using System;

class Program
{
    static void Main()
    {
        Console.Write("Enter a value: ");
        string input = Console.ReadLine();

        // Convert to Integer
        if (int.TryParse(input, out int intValue))
        {
            Console.WriteLine($"Integer Value: {intValue}");
        }
        else if (double.TryParse(input, out double doubleValue))  // Convert to Double
        {
            Console.WriteLine($"Double Value: {doubleValue}");
        }
        else if (decimal.TryParse(input, out decimal decimalValue))  // Convert to Decimal
        {
            Console.WriteLine($"Decimal Value: {decimalValue}");
        }
        else if (bool.TryParse(input, out bool boolValue))  // Convert to Boolean
        {
            Console.WriteLine($"Boolean Value: {boolValue}");
        }
        else if (DateTime.TryParse(input, out DateTime dateValue))  // Convert to DateTime
        {
            Console.WriteLine($"DateTime Value: {dateValue}");
        }
        else
        {
            Console.WriteLine("Could not convert the input.");
        }
    }
}
