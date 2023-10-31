N,M = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
for i in range(N):
    print(' '.join([str(a+b) for a,b in zip(list(map(int,input().split())),A[i])]))