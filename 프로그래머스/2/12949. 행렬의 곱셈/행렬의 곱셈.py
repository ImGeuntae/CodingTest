def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        L = []
        for j in range(len(arr2[0])):
            l = [arr2[x][j] for x in range(len(arr2))]
            L.append(sum([a*b for a,b in zip(l,arr1[i])]))
        answer.append(L)
    return answer