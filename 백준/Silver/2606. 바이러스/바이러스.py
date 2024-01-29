C = {k:[] for k in range(1,int(input())+1)}
for _ in range(int(input())):
    a,b = map(int,input().split())
    C[a] += [b]
    C[b] += [a]
Q = [1]
s = set()
while Q:
    n = Q.pop(0)
    if n not in s:
        s.add(n)
        Q.extend(C[n])
print(len(s)-1)