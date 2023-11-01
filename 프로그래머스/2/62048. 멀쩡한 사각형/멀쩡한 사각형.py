def solution(w,h):
    a,b = w,h
    while w and h:
        w,h = max(w,h)%min(w,h), min(w,h)
    return(a*b-(a+b-h))