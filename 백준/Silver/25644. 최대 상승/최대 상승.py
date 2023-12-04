import sys
input()
ans,low = -1,1e10
for a in map(int,sys.stdin.readline().split()):
    if a<low:
        low = a
    ans = max(ans,a-low)
print(ans)