L = [1,1,2,2,2,8]
l = list(map(int,input().split()))
print(' '.join([str(a-b) for a,b in zip(L,l)]))