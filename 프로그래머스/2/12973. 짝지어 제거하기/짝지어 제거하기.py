def solution(s):
    stack = []
    for i in s:
        if not stack or stack[-1] != i:
            stack.append(i)
        else:
            stack.pop()
    return 1 if not stack else 0