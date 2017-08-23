#include <stdio.h>
//merge sort 
//a[begin...mid],a[mid...end]=>a[begin...end]
void mergeArray(int a[],int begin,int mid,int end,int temp[])
{
    int i ,j,k;
    i = begin;
    j = mid+1; 
    k = 0;
    while(i <= mid && j <= end)
    {
        if(a[i] < a[j])
            temp[k++] = a[i++];
        else
            temp[k++] = a[j++];
    }
    while(i < mid)
        temp[k++] = a[i++];
    while(j < end)
        temp[k++] = a[j++];
    for( i = 0;i < k;i++)
        a[begin + i] = temp[i];
}
void mergeSort(int a[],int n,int m,int temp[])
{
    if(n<m)
    {
        mid = (m + n)/2;
        mergeSort(a,n,mid,temp);
        mergeSort(a,mid+1,m,temp);
        mergeArray(a,n,mid,m,temp);
    }

}