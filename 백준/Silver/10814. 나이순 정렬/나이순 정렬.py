import sys
input()
L = [i.split() for i in sys.stdin]
for i in sorted(L,key=lambda x:int(x[0])):
    print(*i)