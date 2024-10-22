#include<stdio.h>
int main()
{
    int n;
    printf("Enter size of Array : ");
    scanf("%d",&n);
    int a[n],i,j;
    printf("Enter elements in the array : \n");
    for(i=0;i<n;i++)
    {
           scanf("%d",&a[i]);
    }
    printf("Array before sorting : ");
    for(i=0;i<n;i++)
    {
        printf("%d ",a[i]);
    }
    for(i=0;i<n-1;i++)
    {
        for(j=0;j<n-i-1;j++)
        {
            if(a[j]>a[j+1])
            {
                int temp=a[j];
                a[j]=a[j+1];
                a[j+1]=temp;
            }
        }
    }
    printf("\nArray after sorting : ");
    for(i=0;i<n;i++)
    {
        printf("%d ",a[i]);
    }
}
