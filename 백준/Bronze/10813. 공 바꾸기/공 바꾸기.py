N,M = map(int,input().split())
B = [str(x+1) for x in range(N)]
for _ in range(M):
    i,j = map(int,input().split())
    B[i-1], B[j-1] = B[j-1], B[i-1]
print(' '.join(B))