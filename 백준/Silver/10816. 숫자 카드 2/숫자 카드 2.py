from collections import defaultdict as dd
input()
import sys
d = dd(int)
for i in sys.stdin.readline().split():
    d[i] += 1
input()
print(*[d[i] for i in sys.stdin.readline().split()])