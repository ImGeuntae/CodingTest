import sys
from collections import Counter as c
n = int(input())
L = [int(i) for i in sys.stdin]
L.sort()
print(round(sum(L)/n))
print(L[n//2])
print(c(L).most_common(2)[1][0] if len(c(L))>1 and c(L).most_common(2)[0][1] == c(L).most_common(2)[1][1] else c(L).most_common(1)[0][0])
print(L[-1]-L[0])