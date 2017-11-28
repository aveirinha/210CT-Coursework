#include <stdio.h>
#include <stdlib.h>


int multiply(int deg1, int p1[], int deg2, int p2[])
{
  if(p1 == NULL || p2 == NULL)
    return 0;

    int res[deg1+deg2+1];
    int deg3 = deg1 + deg2;

    for(int i = 0; i < deg3+1; i++)
        res[i] = 0;

   for(int i = 0; i <= deg1; i++)
   {
       for(int j = 0; j <= deg2; j++)
       {
            res[i+j] = res[i+j] + p1[i]*p2[j];
       }
   }

    printf("Degree = %d  P3 = ", deg3);
    for(int i = 0; i < deg3+1; i++)
        printf("%d, ", res[i]);


    return 0;

}

int main()
{
    int deg1 = 2;
    int p1[] = {};
    int deg2 = 3;
    int p2[] = {2,1,2,1};

    multiply(deg1, p1, deg2, p2);

    return 0;
}