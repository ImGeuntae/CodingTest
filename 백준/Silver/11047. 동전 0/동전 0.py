import sys
N,K = map(int,input().split())
coin = [int(sys.stdin.readline()) for i in range(N)]
ans = 0
for i in coin[::-1]:
    ans += K//i
    K = K%i
print(ans)