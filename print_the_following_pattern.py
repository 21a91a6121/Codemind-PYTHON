n = int(input())
for row in range(n):
    for col in range(n):
        print(chr(65+row),end=" ")
    print()