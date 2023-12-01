for _ in range(int(input())):
    N,M = map(int,input().split())
    L = [1]*(M-N+1)
    for _ in range(N-1):
        n = 0
        for i in range(M-N+1):
            L[i] = n = n+L[i]
    print(sum(L))