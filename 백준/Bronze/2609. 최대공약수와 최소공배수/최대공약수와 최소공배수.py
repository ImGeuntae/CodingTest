a,b=map(int,input().split())
n=a*b
while b:
    a,b=b,a%b
print(a)
print(n//a)