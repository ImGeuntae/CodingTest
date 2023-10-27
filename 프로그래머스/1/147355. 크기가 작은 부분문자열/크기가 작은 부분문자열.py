def solution(t, p):
    X = [t[i:i+len(p)] for i in range(len(t)-len(p)+1)]
    return len([x for x in X if int(p)>=int(x)])
    