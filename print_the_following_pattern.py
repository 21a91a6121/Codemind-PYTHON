n = int(input())
ch = 64
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(chr(i+ch),end=" ")
    print()