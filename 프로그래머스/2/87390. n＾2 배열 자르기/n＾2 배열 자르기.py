def solution(n, left, right):
    answer = []
    Z = list(range(1,n+1))
    for i in range(left,right+1):
        answer.append(max((i//n)+1,Z[i%n]))
    return answer