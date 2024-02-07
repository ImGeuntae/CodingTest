import heapq
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    H,h,V,i = [],[],[],0
    for _ in range(int(input())):
        x = input()
        if x == 'D 1\n':
            while H and V[H[0][1]]:
                heapq.heappop(H)
            if H:
                V[heapq.heappop(H)[1]] = True
        elif x == 'D -1\n':
            while h and V[h[0][1]]:
                heapq.heappop(h)
            if h:
                V[heapq.heappop(h)[1]] = True
        else:
            x = int(x.split()[1])
            heapq.heappush(H,(-x,i))
            heapq.heappush(h,(x,i))
            V += [False]
            i += 1
    while H and V[H[0][1]]:
        heapq.heappop(H)
    while h and V[h[0][1]]:
        heapq.heappop(h)
    if H:
        print(*(-H[0][0],h[0][0]))
    else:
        print("EMPTY")