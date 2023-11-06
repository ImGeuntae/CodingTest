def solution(money):
    h = len(money)
    M, m = [0]*(h-1), [0]*h
    M[0] = M[1] = money[0]
    for i in range(2,h-1):
        M[i] = max(money[i]+M[i-2], M[i-1])
    m[0], m[1] = 0, money[1]
    for j in range(2,h):
        m[j] = max(money[j]+m[j-2], m[j-1])
    return max(M[-1], m[-1])