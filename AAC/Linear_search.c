#include<stdio.h>
int main()
{
    int n;
    printf("Enter size of array : ");
    scanf("%d",&n);
    int a[n],i,j;
    printf("Enter elements in array : " );
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    printf("Enter element to be searched : ");
    int key;
    scanf("%d",&key);
    for(i=0;i<n;i++)
    {
        if(a[i]==key)
        {
            printf("%d found at %d",key,i+1);
        }
    }
}