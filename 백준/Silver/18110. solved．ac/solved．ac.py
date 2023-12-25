import sys
if (n:=int(input())):
    L = [int(i) for i in sys.stdin]
    L.sort()
    if (a:=int(n*0.15+0.5)):
        s = sum(L[a:-a])
    else:
        s = sum(L)
    print(int(s/(n-2*a)+0.5))
else:
    print(0)