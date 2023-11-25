n = int(input())
a,b,c = n//5, (n%5)//2, (n%5)%2
if c:
    a -= 1
    b += 3
if a<0:
    print(-1)
else:
    print(a+b)