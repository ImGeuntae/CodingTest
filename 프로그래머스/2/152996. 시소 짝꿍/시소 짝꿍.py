from collections import Counter
def solution(weights):
    ans, C = 0, Counter(weights)
    for i in C:
        ans += C[i] * (C[i] - 1) // 2
        ans += C[i] * C[i * 3 / 2]
        ans += C[i] * C[i * 2]
        ans += C[i] * C[i * 4 / 3]
    return ans