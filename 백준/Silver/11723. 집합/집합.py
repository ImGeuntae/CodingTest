import sys
input()
S = set()
for i in sys.stdin:
    if i[0]=='e':
        S.clear()
    elif i[1]=='l':
        S = set(range(1,21))
    else:
        c,n = i.split()
        n = int(n)
        if c[0]=='a':
            S.add(n)
        elif c[0]=='r':
            S.discard(n)
        elif c[0]=='c':
            print(1*(n in S))
        else:
            try:
                S.remove(n)
            except:
                S.add(n)