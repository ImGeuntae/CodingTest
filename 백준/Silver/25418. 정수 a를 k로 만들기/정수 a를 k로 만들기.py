A,K= map(int,input().split())
n = 0
while K!=A:
    if K/2 < A:
        n += K-A
        break
    elif K%2:
        K = (K-1)//2
        n += 2
    else:
        K //= 2
        n += 1
print(n)