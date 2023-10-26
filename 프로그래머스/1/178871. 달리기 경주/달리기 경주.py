def solution(players, callings):
    rank = {name: n for n, name in enumerate(players)}
    for i in callings:
        r = rank[i]
        rank[i] -= 1
        rank[players[r-1]] += 1
        players[r-1],players[r] = players[r], players[r-1]
    return players
        