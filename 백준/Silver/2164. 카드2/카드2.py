import math
n=int(input())
print(1 if n==1 else (n-2**int(math.log2(n-1)))*2)