def solution(prices):
    l = len(prices)
    answer = [0 for _ in range(l)]
    for i in range(l-2):
        k = 1
        j = i+1
        while (prices[i] <= prices[j]):
            k += 1
            j += 1
            if k == l-1-i:
                break
        answer[i] = k
    answer[-2] = 1
    return answer