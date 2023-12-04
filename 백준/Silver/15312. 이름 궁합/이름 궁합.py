N = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
R = sum([[N[ord(a)-65],N[ord(b)-65]] for a,b in zip(input(),input())],[])
for i in range(len(R)-1,1,-1):
    R = [(R[idx]+R[idx+1])%10 for idx in range(i)]
print(''.join(map(str,R)))