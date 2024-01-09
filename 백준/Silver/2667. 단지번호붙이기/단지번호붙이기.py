N = int(input())
M = [[*input()] for _ in range(N)]
P = []
for i in range(N):
    for j in range(N):
        if M[i][j]=='1':
            P += [1]
            Q = [(i,j)]
            M[i][j] = '0'
            while Q:
                x,y = Q.pop(0)
                for a,b in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                    if 0<=a<N and 0<=b<N and M[a][b]=='1':
                        P[-1] += 1
                        M[a][b]='0'
                        Q += [(a,b)]
print(len(P),*sorted(P),sep='\n')