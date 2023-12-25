import sys
if (n:=int(input())):
    L = sorted(int(i) for i in sys.stdin)
    a = int(n*0.15+0.5)
    print(int(sum(L[a:n-a])/(n-2*a)+0.5))
else:
    print(0)