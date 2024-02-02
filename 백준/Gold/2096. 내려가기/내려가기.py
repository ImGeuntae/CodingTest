import sys
m,M = [0]*3,[0]*3
input()
for i in sys.stdin:
    a,b,c = map(int,i.split())
    m = [min(m[:2])+a,min(m)+b,min(m[1:])+c]
    M = [max(M[:2])+a,max(M)+b,max(M[1:])+c]
print(max(M),min(m))