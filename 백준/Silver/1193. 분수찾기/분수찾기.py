N = int(input())
n = 1
while N>n:
    N -= n
    n += 1
if n%2:
    print("{}/{}".format(n-N+1,N))
else:
    print("{}/{}".format(N,n-N+1))