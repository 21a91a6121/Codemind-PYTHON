num = int(input())
largest = 0
while num!=0:
    rem = num%10
    if rem>largest:
        largest = rem
    num = num//10
print(largest)
