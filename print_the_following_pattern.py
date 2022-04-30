n = int(input())
for row in range(n+1,1,-1):
    for col in range(1,row):
        print(col,end="")
    print()
        