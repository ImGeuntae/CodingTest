def solution(order):
    answer, stack = 0, []
    for idx in range(1,len(order)+1):
        stack.append(idx)
        while stack and stack[-1]==order[answer]:
            stack.pop()
            answer += 1
    return answer