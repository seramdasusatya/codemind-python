n=int(input())
arr=list(map(int,input().split()))
s1=0
s2=0
for i in range(n):
    if arr[i]%2==0:
        s1=s1+arr[i]
    elif arr[i]%2==1:
        s2=s2+arr[i]
print(abs(s1-s2))      