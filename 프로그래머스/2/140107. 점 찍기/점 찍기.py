def solution(k, d):
    ans = 0
    for i in range(0,d+1,k):
        ans += int((((d**2)-(i**2))**0.5)//k) + 1
    return ans