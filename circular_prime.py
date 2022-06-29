n=int(input())
c=0
for i in range(1,n+1):
    if(n%i==0):
        c=c+1
rev=0        
while(n!=0):
    d=n%10
    rev=rev*10+d
    n=n//10
k=0
for j in range(1,rev+1):
    if(rev%j==0):
        k=k+1
if(c==2 and k==2):
    print("circular prime")
elif(c==2 and k!=2):
    print("prime but not a circular prime")
else:
    print("not prime")