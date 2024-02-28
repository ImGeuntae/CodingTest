N,M = map(int,input().split())
t,*T = map(int,input().split())
T = set(T)
P = []
F = []
def f(s1,s2):
    S = []
    for s in s2:
        if s&s1:
            s1 = s|s1
            s1,S = f(s1,S)
        else:
            S += [s]
    return s1,S        
for _ in range(M):
    _,*p = map(int,input().split())
    P += [set(p)]
T,F = f(T,P)
print(len(F))