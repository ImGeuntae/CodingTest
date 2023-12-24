from collections import deque
for _ in range(int(input())):
    N,M = map(int,input().split())
    L = deque(map(int,input().split()))
    p,ans = L[M],0
    while True:
        for i in L:
            if i>L[0]:
                L.append(L.popleft())
                break
        else:
            N -= 1
            ans += 1
            if L.popleft() == p and M == 0:
                print(ans)
                break
        M = (M-1)%N