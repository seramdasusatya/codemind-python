n=int(input())
arr=list(map(int,input().strip().split()))
c=0
b=[]
for i in range(n):
    c=0
    for j in range(n):
        if(arr[i]==arr[j]):
            c=c+1
        if(c==arr[i]):
            b.append(arr[i])
if len(b)==0:
    print("-1")
else:    
    print(min(b),end=" ")
    print(max(b),end="")