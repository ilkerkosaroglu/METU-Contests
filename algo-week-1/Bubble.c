#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int i,sz;
int count=0;
int bub(int * arr,int siz);
int main() {
    int arr[1005];
    scanf("%d",&sz);
    for(i=0;i<sz;i++){
        scanf("%d",&arr[i]);
    }
    bub(arr,sz);
    printf("%d\n",count);
    return 0;
}
int bub(int *arr,int siz){
    int temp,flag;
    flag=1;
    while(flag){
        flag=0;
        for(i=0;i<siz-1;i++){
            if(arr[i]>arr[i+1]){
                flag=1;
                count++;
                temp=arr[i+1];
                arr[i+1]=arr[i];
                arr[i]=temp;
            }
        }
        
    }
    return 0;   
}

