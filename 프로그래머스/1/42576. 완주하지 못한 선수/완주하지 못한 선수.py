def solution(participant, completion):
    h = sum([hash(i) for i in participant]) - sum([hash(j) for j in completion])
    return [k for k in participant if hash(k)==h][0]
    