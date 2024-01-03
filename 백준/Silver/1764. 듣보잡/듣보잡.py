import sys
N,M = map(int,input().split())
D = [i.strip() for i in sys.stdin]
L = set(D[:N])&set(D[N:])
print(len(L),*sorted(L))