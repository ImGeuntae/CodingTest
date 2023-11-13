def solution(n, computers):
    C = [x for x in range(n)]
    answer = 0
    while C:
        visited = []
        queue = []
        queue.append(C[0])
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.append(node)
                queue.extend([idx for idx, i in enumerate(computers[node]) if i==1 and idx!=node])
        answer += 1
        C = [x for x in C if x not in visited]
    return answer
        