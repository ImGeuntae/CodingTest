D,K = map(int,input().split())
a=b=x=1
for _ in range(D-3):
    a,b = b,a+b
while (K-a*x)%b:
    x += 1
print(x)
print((K-a*x)//b)