using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;

namespace Q1
{
    internal class Program
    {

        void Q1()
        {

            Console.WriteLine("Welcome\n" +
                "Byee!!!");
            Console.Write("Happy Journey!!");

        }


        void Q2()
        {
            Console.WriteLine ("Enter your name:");
            string name= Console.ReadLine();

            Console.WriteLine("Enter your age:");
            int age = Convert.ToInt32( Console.ReadLine());

            Console.WriteLine("Enter your profession:");
            string profession = Console.ReadLine();

            Console.WriteLine("Enter your fav color:");
            string colour= Console.ReadLine();
            Console.WriteLine($"Hello {name}!\nyour age is {age} ,your fav color is {colour}\nand you work as {profession}" );



        }

        void Q3()
        {
            string s, c;
            for (int i = 1; i < 11; i++)
            {
                s = (i * i).ToString().PadLeft(6,'0');
                Console.WriteLine($"Square of {i}:{s}");
                
            }
            Console.WriteLine();
            for (int i = 1; i < 11; i++)
            {
                c = (i * i*i).ToString().PadLeft(6, '0');
                Console.WriteLine($"Cube of {i}:{c}");
            }
        }



       void Q4()
        {
            bool b = true;
            while (b)
            {
                try
                {
                    int num = Convert.ToInt32(Console.ReadLine());
                    b = false;
                }
                catch (Exception e)
                {

                    Console.WriteLine(e.Message);
                }
            }
        }

        void Q5()
        {
            Random r = new Random();

            int ans = r.Next(1, 11);
            Console.Write(ans);
            int cnt = 0;
            while (cnt<3)
            {
                Console.WriteLine("Enter number 1 to 10");
                int num = Convert.ToInt32(Console.ReadLine());

               
                if (num == ans)
                {
                    Console.WriteLine("Yeah! You Gussed the number..");
                }
                else if (num < ans)
                {
                    Console.WriteLine("Number gussed is smaller than answer");
                }
                else
                {
                    Console.WriteLine("Number gussed is greater than answer");
                }
                cnt++;

            }

            Console.WriteLine("Game exit\n");
        }

        void Q6()
        {
            int age = 0;
            string name = "";
            string profession = "";
            while (true)
            {
                Console.WriteLine("Enter your choice : \n1.Fill info\n2.Display info");
                int choice = Convert.ToInt32(Console.ReadLine());
                
                switch (choice)
                {
                    case 1:
                        Console.WriteLine("Enter your name:");
                         name = Console.ReadLine();

                        Console.WriteLine("Enter your age:");
                        age = Convert.ToInt32(Console.ReadLine());

                        

                        Console.WriteLine("Enter your profession:");
                        profession = Console.ReadLine();
                        Console.WriteLine($"Hello {name}!\nyour age is {age} and you work as {profession}");
                        break;
                    case 2:
                        Console.WriteLine($"Hello {name}!\n{(age > 18 ? "You are an Adult" : "You are a Teenager")}\nyour age is {age},\nand you work as {profession}");

                        break;
                }

            }
        }

        void Q7()
        {
            int a = Convert.ToInt32(Console.ReadLine());
            int b = Convert.ToInt32(Console.ReadLine());

            while (true)
            {
                Console.WriteLine("Enter your choice : \n1Addition\n2.Subtraction\n3.Multiplication\n4.Division\n ");
                int choice = Convert.ToInt32(Console.ReadLine());

                switch (choice)
                {
                    case 1:
                        Console.WriteLine($"Addition :{a + b}");

                        break;
                    case 2:
                        Console.WriteLine($"Subtraction :{a - b}");

                        break;
                    case 3:
                        Console.WriteLine($"Multiplication :{a * b}");

                        break;
                    case 4:
                        Console.WriteLine($"Division :{a / b}");

                        break;
                }
            }

        }
        static void Main(string[] args)
        {
            Program p=new Program();
            /*  p.Q1();*/
            /*p.Q2();
            p.Q3();
            p.Q4();
            p.Q5();
            p.Q6();*/
            p.Q7();
            Console.ReadKey();
        }
    }
}
