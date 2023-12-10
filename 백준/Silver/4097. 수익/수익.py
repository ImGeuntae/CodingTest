import sys
while n:=int(input()):
    dp=ans=-10000
    for i in map(int,[sys.stdin.readline() for _ in range(n)]):
        dp=max(i,i+dp)
        ans=max(ans,dp)
    print(ans)