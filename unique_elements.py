n=int(input())
arr=list(map(int,input().split()))
b=[]
for i in arr:
    if i not in b:
        b.append(i)
    else:
        continue
print(*b)
