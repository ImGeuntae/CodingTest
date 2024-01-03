import sys
L = [0]*10001
input()
for i in sys.stdin:
    L[int(i)] += 1
for i in range(1,10001):
    for _ in range(L[i]):
        print(i)