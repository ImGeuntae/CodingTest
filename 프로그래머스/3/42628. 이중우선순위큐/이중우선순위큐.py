from heapq import heappush, heappop, nsmallest
def solution(operations):
    answer = []
    for i in operations:
        if i[0] == "I":
            heappush(answer,int(i[2:]))
        elif answer and i[-2] == "-":
            heappop(answer)
        elif answer and i[-2] == " ":
            answer = nsmallest(len(answer)-1,answer)
    return [max(answer), min(answer)] if answer else [0,0]