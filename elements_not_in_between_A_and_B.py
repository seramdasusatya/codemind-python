n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
k=0
f=0
for i in range(len(arr)):
    k=0
    if(arr[i]>=a and arr[i]<=b):
        k=1
    if(k==0):
        f=1
        print(arr[i],end=" ")
if(f==0):
    print("-1")