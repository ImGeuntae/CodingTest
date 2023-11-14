import sys
N,M = map(int,input().split())
ans,L = [],[]
for _ in range(M):
    L.append(list(sys.stdin.readline().split()))
for x in sorted(L,key=lambda x:(x[0],x[1])):
    x = set(x)
    for s in ans:
        if x&s:
            s.update(x)
            break
    else:
        ans.append(x)
print(len(ans) + N - sum([len(i) for i in ans]))