def solution(n, stations, w):
    answer, x = 0, 1
    while x<=n:
        if x < stations[0]-w:
            answer += 1
            x += 2*w + 1
        else:
            x = stations[0]+w+1
            stations.pop(0)
            if not stations:
                return answer-(-(n-x+1)//(2*w+1))
    return answer