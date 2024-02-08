G = {}
for _ in range(int(input())):
    a,b,c = input().split()
    G[a] = [b,c]
def X(A,G):
    a=b=c=d=e=f=''
    if G[A][0] != '.':
        a,b,c = X(G[A][0],G)
    if G[A][1] != '.':
        d,e,f = X(G[A][1],G)
    return [A+a+d,b+A+e,c+f+A]
print(*X('A',G))

