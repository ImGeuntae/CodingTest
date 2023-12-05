a=b=1
for _ in range(int(input())-1):
    a,b = b,(b+2*a)%10007
print(b)