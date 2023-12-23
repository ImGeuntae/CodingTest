import sys
n = int(input())
N,L,ans = list(range(1,n+1)),[0],[]
for i in map(int,sys.stdin):
    while L[-1]!=i and N:
        L += [N.pop(0)]
        ans += ["+"]
    if L[-1]==i:
        L.pop()
        ans += ["-"]
    else:
        print("NO")
        break
else:
    print(*ans)