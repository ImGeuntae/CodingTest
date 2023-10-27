def solution(a, b):
    a,b = min(a,b), max(a,b)
    return sum([n for n in range(a,b+1)])
    