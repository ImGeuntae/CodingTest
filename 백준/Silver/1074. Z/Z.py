N,r,c = map(int,input().split())
ans,n = 0, 2**(N-1)
for _ in range(N):
    ans += n*n*(2*(r>=n)+(c>=n))
    n,r,c = n//2, r%n, c%n
print(ans)