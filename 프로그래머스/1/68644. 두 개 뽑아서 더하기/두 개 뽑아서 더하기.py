def solution(numbers):
    s = set()
    for i in range(len(numbers)-1):
        for j in numbers[i+1:]:
            s.add(numbers[i] + j)
    return sorted(list(s))