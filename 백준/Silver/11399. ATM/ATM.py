n = int(input())
L = sorted(list(map(int,input().split())))
print(sum([L[i]*(n-i) for i in range(n)]))