import sys
L = [0] * 10001
for _ in range(int(input())):
    n = int(sys.stdin.readline())
    L[n] += 1
for i in range(1,10001):
    if L[i]:
        for _ in range(L[i]):
            print(i)