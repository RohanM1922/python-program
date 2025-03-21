#include<stdio.h>
int main(){
    int a,b,c,avg;
    printf("enter 1st number= ");
    scanf("%d",&a);
    printf("enter 2nd number= ");
    scanf("%d",&b);
    printf("enter 3rd number= ");
    scanf("%d",&c);
    avg=(a+b+c)/3;
    printf("average of number is= %f",avg);
    return 0;
}