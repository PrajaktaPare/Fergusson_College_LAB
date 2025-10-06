using System;

class Program
{
    static void Main()
    {
        Console.Write("Enter a string: ");
        string input = Console.ReadLine();

        // Apply String Functions
        string upperCase = input.ToUpper();  // Convert to Uppercase
        string lowerCase = input.ToLower();  // Convert to Lowercase
        string trimmed = input.Trim();  // Remove Leading and Trailing Spaces
        string replaced = input.Replace('e', 'E');  // Replace 'e' with 'E'

        // Find occurrences of 'l'
        int count = 0;
        Console.Write("Positions of 'l': ");
        for (int i = 0; i < input.Length; i++)
        {
            if (input[i] == 'l')
            {
                count++;
                Console.Write(i + " ");
            }
        }
        Console.WriteLine($"\nNumber of times 'l' appears: {count}");

        // Transform String into *H*e*l*l*o format
        string formatted = "*" + string.Join("*", input.ToCharArray()) + "*";
        Console.WriteLine($"Formatted Output: {formatted}");
    }
}
