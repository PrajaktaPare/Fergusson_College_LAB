#include<stdio.h>
int magicsqurare(int n)
{
    int temp[n][n];
    int c=n/2;//column
    int r=0;//row
    int i,j;
    for( i=0;i<n;i++)
    {
        for( j=0;j<n;j++)
        {
             temp[i][j]=0;
        }
        printf("\n");
    }
    for(i=1;i<=n*n;i++)
    {
        temp[r][c]=i;
        int nr=((n+r)-1)%n;//newcolumn
        int nc=((n+c)-1)%n;//newrow
        if(temp[nr][nc]!=0)
        {
            r=(r+1)%n;
        }
        else{
            r=nr;
            c=nc;
        }
    }  
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            printf("%d ",temp[i][j]);
        }
        printf("\n");
    }
}
int main()
{
    int n;
    printf("Enter Order of magic square : ");
    scanf("%d",&n);
    magicsqurare(n);
}