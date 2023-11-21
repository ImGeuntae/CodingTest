def solution(sequence):
    A = B = ans1 = ans2 = float("-inf")
    for a,b in [(n,-n) if (idx%2) else (-n,n) for idx,n in enumerate(sequence)]:
        A, B = max(a, a+A), max(b, b+B)
        ans1, ans2 = max(ans1,A), max(ans2,B)
    return max(ans1,ans2)