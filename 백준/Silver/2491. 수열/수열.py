import sys
input()
ans = u = d = 1
x = -1
for n in map(int,sys.stdin.readline().split()):
    if x == -1:
        x = n
        continue
    if x <= n:
        u += 1
    else:
        ans,u = max(ans,u),1
    if x >= n:
        d += 1
    else:
        ans,d = max(ans,d),1
    x = n
print(max(ans,u,d))