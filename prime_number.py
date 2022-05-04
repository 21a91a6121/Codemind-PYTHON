n = int(input())
c=1
for i in range(2,n):
    if n%i==0:
        c=c+1
if c>1:
    print("not a prime")
else:
    print("prime")
        