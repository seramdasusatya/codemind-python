n=int(input())
arr=list(map(int,input().split()))
s=0
for i in range(len(arr)):
    s=sum(arr)
avg=s/len(arr)
if int(avg) in arr:
    print("True")
else:
    print("False")