N,M = map(int, input().split())
L = [str(i+1) for i in range(N)]
for _ in range(M):
    i,j = map(int, input().split())
    L[i-1:j] =  L[i-1:j][::-1]
print(' '.join(L))