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
   for(i=1;i<n;i++)
   {
       int key=a[i];
       int j=i-1;
       while(j>=0 && a[j]>key)
       {
           a[j+1]=a[j];
           
           j=j-1;
       }
       a[j+1]=key;
   }
    printf("\nArray after sorting : ");
    for(i=0;i<n;i++)
    {
        printf("%d ",a[i]);
    }
}
