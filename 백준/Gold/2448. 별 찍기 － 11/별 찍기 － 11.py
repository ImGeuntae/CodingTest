import math
N = int(input())
S = ["  *  "," * * ","*****"]
for _ in range(int(math.log2(N//3))):
    x = len(S)
    S = [" "*x+s+" "*x for s in S] + [s+" "+s for i,s in enumerate(S)]
print(*S,sep='\n')