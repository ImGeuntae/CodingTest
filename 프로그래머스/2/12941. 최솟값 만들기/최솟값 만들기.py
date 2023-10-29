def solution(A,B):
    A, B = sorted(A), sorted(B,reverse=True)
    answer = 0
    for i in range(len(A)):
        answer += A[i]*B[i]
    return answer