from itertools import permutations as p
N,M = map(int,input().split())
L = sorted(map(int,input().split()))
for i in p(L,M):
    print(*i)