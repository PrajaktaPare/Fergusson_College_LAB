using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection.Emit;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Serialization;

namespace Ass2q1
{
    internal class Student
    {
        string name;
        int age;
        char grade;

        Student(string name, int age, char grade)
        {
            this.name = name;   
            this.age = age;
            this.grade = grade;
        }

        public void display()
        {
            Console.WriteLine($"Name : {name} \nAge : {age}\nGrade : {grade}");
        }



        static void Main(string[] args)
        {
            Student s = new Student("PP", 20, 'A');
            s.display();
            Console.ReadKey();
        }
    }
}
