#!/bin/python3

import sys

def beautifulTriplets(d, arr,n):
    # Complete this function
    triplet=[0 for i in range(3)]
    c=0
    for i in range(n-3):
        k=0
        for j in range(i+1,n-2):
            if abs(arr[j]-arr[i])==d:
                triplet[k]=arr[i]
                triplet[k+1]=arr[j]
                k=k+2
            
                for u in range(j+1,n):
                    if(abs(arr[u]-arr[j]))==d:
                
                        triplet[k]=arr[u]
                        c=c+1
                    
       '''
    c=0
    for i in range(n):
        if arr[i]+d in arr and arr[i]+2*d in arr:
            c=c+1
    return c

    '''

if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    arr = list(map(int, input().strip().split(' ')))
    result = beautifulTriplets(d, arr,n)
    print(result)
