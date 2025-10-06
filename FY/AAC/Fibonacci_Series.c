#include<stdio.h>
int main()
{
    int a=0,b=1,c,n,i;
    printf("Enter the number : ");
    scanf("%d",&n);
    printf("Fibonacci Series is : %d %d ",a ,b);
    for(i=3;i<=n;i++)
    {
        c=a+b;
        printf("%d ",c);
        a=b;
        b=c;
    }
}
