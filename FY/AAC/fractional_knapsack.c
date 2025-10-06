
#include <stdio.h>

int main() {
    int n, capacity;
    printf("Enter number of items: ");
    scanf("%d", &n);
    printf("Enter capacity of sack:\n");
    scanf("%d", &capacity);

    int p[n], w[n];
    float pbyw[n];
    int index[n];

    printf("Enter P and W values of each item (value and weight):\n");
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &p[i], &w[i]);
        pbyw[i] = (float)p[i] / w[i]; 
        index[i] = i; 
    }

    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (pbyw[j] < pbyw[j + 1]) { 
                float temp = pbyw[j + 1];
                pbyw[j + 1] = pbyw[j];
                pbyw[j] = temp;

                int tempW = w[j + 1];
                w[j + 1] = w[j];
                w[j] = tempW;

                int tempIndex = index[j + 1];
                index[j + 1] = index[j];
                index[j] = tempIndex;
            }
        }
    }
    for(int i=0;i<n;i++)
    {
        printf("%f ",pbyw[i]);
    }
    
    float totalProfit = 0.0;
    int rem = capacity;
    for (int i = 0; i < n; i++) {
        int itemIndex = index[i];
        if (w[itemIndex] <= rem) {
            totalProfit += p[itemIndex]; 
            rem -= w[itemIndex];
        } else {
            totalProfit += p[itemIndex] * ((float)rem / w[itemIndex]);
            break; 
        }
    }

    printf("\nMaximum Profit is: %.2f\n", totalProfit);
    return 0;
}
