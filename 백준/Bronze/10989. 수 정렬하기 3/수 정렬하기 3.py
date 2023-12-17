import sys
L = [0] * 10001
for _ in range(int(input())):
    L[int(sys.stdin.readline())] += 1
for i in range(1,10001):
    if L[i]:
        for _ in range(L[i]):
            print(i)