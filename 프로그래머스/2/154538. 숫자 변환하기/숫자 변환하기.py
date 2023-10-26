def solution(x, y, n):
    L = {x}
    answer = 0
    while True:
        if y in L:
            return answer
        else:
            N = set()
            N.update([i+n for i in L if (i+n<=y)])
            N.update([i*2 for i in L if (i*2<=y)])
            N.update([i*3 for i in L if (i*3<=y)])
            L = list(N)
            answer += 1
        if not N:
            return -1
                