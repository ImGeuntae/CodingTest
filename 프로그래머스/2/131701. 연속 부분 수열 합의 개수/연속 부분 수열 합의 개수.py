def solution(elements):
    L = elements[:]
    answer = elements[:]
    for _ in range(1,len(elements)-1):
        elements.append(elements.pop(0))
        L = [x+y for x,y in zip(L, elements)]
        answer.extend(L)
    return len(set(answer))+1