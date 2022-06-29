n=int(input())
arr=list(map(int,input().split()))
k=int(input())
c=0
for i in range(len(arr)):
    if arr[i]==k:
        c=c+1
print(c)        