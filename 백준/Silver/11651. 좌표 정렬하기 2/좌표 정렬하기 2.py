import sys
input()
X = [list(map(int,i.split())) for i in sys.stdin]
for i in sorted(X,key=lambda x:(x[1],x[0])):
    print(*i)