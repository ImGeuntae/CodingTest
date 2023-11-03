N = int(input())

a = N//5
b = (N%5)//3
c = (N%5)%3

if c == 2:
    a -= 2
    b += 4
elif c == 1:
    a -= 1
    b += 2
if a<0:
    print("-1")
else:
    print(a+b)