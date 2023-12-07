a=b=1
for _ in range(int(input())):
    a,b=b,(a+b)%10
print(a)