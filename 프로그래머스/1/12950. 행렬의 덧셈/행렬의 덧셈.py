def solution(arr1, arr2):
    answer = []
    for x, y in zip(arr1,arr2):
        answer.append([m+n for m,n in zip(x,y)])
    return answer