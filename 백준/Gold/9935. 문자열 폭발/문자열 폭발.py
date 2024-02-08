S,*B = input(),*input()
n,Q = len(B),[]
for s in S:
    Q += [s]
    if Q[-n:] == B:
        del Q[-n:]    
print(''.join(Q) or 'FRULA')