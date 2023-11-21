def solution(sequence):
    A2 = B2 = ans1 = ans2 = float("-inf")
    for a,b in [(n,-n) if (idx%2) else (-n,n) for idx,n in enumerate(sequence)]:
        A1, A2 = A2, max(a, a+A2)
        B1, B2 = B2, max(b, b+B2)
        ans1, ans2 = max(ans1,A2), max(ans2,B2)
    return max(ans1,ans2)