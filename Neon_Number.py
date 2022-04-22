n = int(input())
sum = 0
sq = n*n
while(sq>0):
    rem = sq%10
    sum = sum+rem
    sq = sq//10
if(sum==n):
    print("Neon Number")
else:
    print("Not Neon Number")