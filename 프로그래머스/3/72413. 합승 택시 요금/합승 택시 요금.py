import heapq
def solution(n, s, a, b, fares):
    answer = 0
    dist = [[float("inf")]*(n+1) for _ in range(3)]
    dist[0][s] = dist[1][a] = dist[2][b] = 0
    route = [[] for _ in range(n+1)]
    for x,y,z in fares:
        route[x] += [(z,y)]
        route[y] += [(z,x)]
    for idx,start in enumerate([s,a,b]):
        H = [(0,start)]
        while H:
            now_cost,now_node = heapq.heappop(H)
            if dist[idx][now_node] >= now_cost:
                for next_cost,next_node in route[now_node]:
                    total_cost = now_cost + next_cost
                    if total_cost < dist[idx][next_node]:
                        dist[idx][next_node] = total_cost
                        heapq.heappush(H,(total_cost,next_node))
    return min(x+y+z for (x,y,z) in zip(*dist))
    
        
