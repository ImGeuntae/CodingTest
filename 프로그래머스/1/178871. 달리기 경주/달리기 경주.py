def solution(players, callings):
    rank = {}
    for num, name in enumerate(players):
        rank[name] = num
    for i in callings:
        r = rank[i]
        p = players[r-1]
        
        players[r] = p
        players[r-1] = i
        
        rank[i] -= 1
        rank[p] += 1
        
    return players
        