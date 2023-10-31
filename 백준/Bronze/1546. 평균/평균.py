N = int(input())
L = list(map(int,input().split()))
M = max(L)
print(sum([x/M*100 for x in L])/N)