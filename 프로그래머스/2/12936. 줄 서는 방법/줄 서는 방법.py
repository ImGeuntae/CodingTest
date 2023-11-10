def solution(n, k):
    f, N, ans = 1, [n for n in range(1,n+1)], []
    for i in range(1,n):
        f *= i
    k -= 1
    for i in range(n-1,0,-1):
        ans.append(N.pop(k//f))
        k, f = k%f, f//i
    return ans+N