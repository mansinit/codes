#DIJKSTRA'S ALGORITHM
p=[0 for i in range(20)]
def dijkstra(a,n):
    s=0
    d=[9999 for i in range(n)]
    visited=[0 for i in range(n)]
    d[s]=0
    visited[s]=1
    t=0
    x=0
    while x<n:
        for j in range(n):
            if a[t][j]!=0 and visited[j]==0:
                if d[j]>p[t]+a[t][j]:
                    d[j]=p[t]+a[t][j]
                    p[j]=d[j]
        d[t]=9999
        min=d[t]
        for i in range(n):
            if d[i]<min:
                min=d[i]
                t=i
        visited[t]=1
        x=x+1
        
n=int(input("enter size"))
a=[[int(input()) for j in range(n)] for i in range(n)]
print(a)
dijkstra(a,n)
k=int(input())
print(p[k])
