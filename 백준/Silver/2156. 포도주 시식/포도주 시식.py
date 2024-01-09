a=b=c=d=e=f=ans=0
for i in range(int(input())):
    t = int(input())
    a,b,c,d,e,f = c,d,e,f,max(a,b,c,d)+t,e+t
    ans = max(ans,e,f)
print(ans)