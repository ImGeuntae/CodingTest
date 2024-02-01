BFS = [0]*100001
a,b = map(int,input().split())
Q = [a]
while (q:=Q.pop(0))!=b:
    for x in [q-1,q+1,2*q]:
        if 0<=x<100001 and BFS[x]==0:
            BFS[x] = BFS[q]+1
            Q += [x]
print(BFS[b])