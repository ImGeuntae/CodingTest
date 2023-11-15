def solution(k, m, score):
    score.sort(reverse=True)
    return sum([m*score[(i+1)*m-1] for i in range(len(score)//m)])