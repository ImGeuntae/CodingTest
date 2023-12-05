a1=a2=b1=b2=0
for _ in range(int(input())):
    n = int(input())
    a1,a2,b1,b2 = b1,b2,max(a1,a2)+n,b1+n
print(max(b1,b2))