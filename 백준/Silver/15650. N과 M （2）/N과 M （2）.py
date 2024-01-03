from itertools import combinations as c
N,M = map(int,input().split())
for i in c(range(1,N+1),M):
    print(*i)