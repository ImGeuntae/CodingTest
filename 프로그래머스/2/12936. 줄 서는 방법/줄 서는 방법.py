def solution(n, k):
    N = [n for n in range(1,n+1)]
    f = 1
    ans = []
    for i in range(1,n):
        f *= i
    k -= 1
    while i:
        ans.append(N.pop(k//f))
        k %= f
        f //= i
        i -= 1
    return ans+N