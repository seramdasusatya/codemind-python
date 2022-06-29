def prime(n):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c=c+1
    if(c==2):
        return 1
    else:
        return 0
n=int(input())
c1=0
c2=0
for i in range(1,n+1):
    if(n%i==0):
        c1=c1+1
    if(n%i==0):
        if(prime(i)):
            c2=c2+1
print(abs(c1-c2))            