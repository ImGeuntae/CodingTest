from collections import deque
N = int(input())
M = [[*input()] for _ in range(N)]
P,Q = [],deque()
for i in range(N):
    for j in range(N):
        if M[i][j]=='1':
            p = 0
            Q += [(i,j)]
            while Q:
                x,y = Q.popleft()
                for a,b in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                    if 0<=a<N and 0<=b<N and M[a][b]=='1':
                        p += 1
                        M[a][b]='0'
                        Q += [(a,b)]
            P += [p+(p==0)]
print(len(P),*sorted(P),sep='\n')