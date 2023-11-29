n,a,b = int(input()),1,0
if n>0:
    for _ in range(0,n):
        a,b = b,(a+b)%1000000000
elif n<0:
    for _ in range(0,n,-1):
        a,b = b,(abs(a-b)%1000000000)*([-1,1][(a>0)])
print(-1*(b<0)+(b>0))
print(abs(b))