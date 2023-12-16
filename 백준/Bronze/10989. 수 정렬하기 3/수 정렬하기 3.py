import sys
N = int(input())
L = [0] * 10001
for _ in range(N):
    n = int(sys.stdin.readline())
    L[n] += 1
for i in range(1,10001):
    if L[i]:
        for _ in range(L[i]):
            print(i)