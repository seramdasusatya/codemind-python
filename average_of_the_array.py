n=int(input())
arr=list(map(int,input().split()))
s=0
for i in range(len(arr)):
    s=sum(arr)
avg=s/len(arr)
print("%.2f"%avg)