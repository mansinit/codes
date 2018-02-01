#!/bin/python3

n=int(input())
k=int(input())
q=int(input())
k=k%n
a=[int(input())for i in range(n)]
for i in range(k):
    temp=a[n-1]
    j=n-1
    while j>0:
        a[j]=a[j-1]
        j=j-1
    a[0]=temp
for i in range(q):
    m=int(input())
    print(a[m])
    
