N,M = map(int,input().split())
A = {input() for _ in range(N)}
B = [i for _ in range(M) if (i:=input()) in A]
print(len(B),*sorted(B))