def solution(n, arr1, arr2):
    return([(format((a1 | a2),'b').zfill(n)).replace("1","#").replace("0"," ") for a1, a2 in zip(arr1,arr2)])