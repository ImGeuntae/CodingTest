def solution(bandage, health, attacks):
    time, h = attacks[0][0], health - attacks[0][1]
    for t,d in attacks[1:]:
        n = t - time - 1
        h = min(health, h + n*bandage[1] + (n//bandage[0])*bandage[2])
        time = t
        h -= d
        if h <= 0:
            return -1
    return h