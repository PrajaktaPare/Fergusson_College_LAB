import java.util.Scanner; 

public class decimalToBinary {   
    public static void main(String[] args) { 

Scanner scan = new Scanner(System.in);


   int num, binaryNum = 0;
   int i = 1, rem;

   num = scan.nextInt();

   while (num != 0)
   {
      rem = num % 2;
      num /= 2;
      binaryNum += rem * i;
      i *= 10;
   }


 System.out.println(binaryNum);
}
}