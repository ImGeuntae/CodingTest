import sys
S = sys.stdin.readline().strip()
B = [*sys.stdin.readline().strip()]
n = len(B)
Q = []
for s in S:
    Q += [s]
    if Q[-n:] == B:
        del Q[-n:]    
print(''.join(Q) if Q else 'FRULA')