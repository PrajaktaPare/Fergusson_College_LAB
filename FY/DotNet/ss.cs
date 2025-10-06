using System;
using System.IO;

class Program
{
    static void Main()
    {
        Console.Write("Enter text to append to the file: ");
        string input = Console.ReadLine();

        string filePath = "sample.txt";  // File name

        // Append text to file
        using (StreamWriter writer = new StreamWriter(filePath, true))  // 'true' for append mode
        {
            writer.WriteLine(input);
        }

        Console.WriteLine("Text appended to file successfully.");
    }
}
