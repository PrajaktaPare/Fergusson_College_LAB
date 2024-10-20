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
   
    for( i=0;i<n-1;i++)
    {
        int minIndex=i;
        for(j=i+1;j<n;j++)
        {
            if(a[j]<a[minIndex])
            {
                minIndex=j;
            }
        }
        int temp=a[i];
        a[i]=a[minIndex];
        a[minIndex]=temp;
    }
    printf("\nArray after sorting : ");
    for(i=0;i<n;i++)
    {
        printf("%d ",a[i]);
    }
}
