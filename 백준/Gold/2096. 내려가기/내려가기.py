N = int(input())
m,M = [0]*3,[0]*3
for _ in range(N):
    a,b,c = list(map(int,input().split()))
    m = [min(m[:2])+a,min(m)+b,min(m[1:])+c]
    M = [max(M[:2])+a,max(M)+b,max(M[1:])+c]
print(max(M),min(m))