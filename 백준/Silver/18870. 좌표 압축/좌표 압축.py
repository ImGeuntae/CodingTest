input()
L = list(map(int,input().split()))
C = sorted(set(L))
ans,n = dict(),0
for i in C:
    ans[i] = n
    n += 1
print(*(ans[i] for i in L))