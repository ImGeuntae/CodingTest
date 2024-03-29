import sys
input()
S = {int(k): int(v) for k,v in [i.split() for i in sys.stdin]}
BFS = [0]*2 + list(range(2,101))
Q = [1]
while Q:
    n = Q.pop(0)
    for x in range(n+1,min(101,n+7)):
        if x in S:
            x = S[x]
        if BFS[x] > BFS[n]+1:
            BFS[x] = BFS[n]+1
            Q += [x]            
print(BFS[-1])