a = b = 1
for _ in range(2,int(input())+1):
    a,b = b,a+b
print(b%10007)