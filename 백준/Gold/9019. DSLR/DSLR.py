import sys
from collections import deque
input()
for i in sys.stdin:
    BFS = ['']*10000
    A,B = map(int,i.split())
    BFS[A] = 'X'
    Q = deque([A])
    while (q:=Q.popleft())!=B:
        for m,x in zip('DSLR',[(2*q)%10000,q-1+(q==0)*10000,(q%1000)*10+(q//1000),(q%10)*1000+(q//10)]):
            if not BFS[x]:
                BFS[x] = BFS[q] + m
                Q += [x]
    print(BFS[q][1:])