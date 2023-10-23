def solution(arr):
    summax = summin = s = 0
    for i in range(len(arr)-2, -1, -2):
        if arr[i] == "+":
            s += int(arr[i+1])
        else:
            summax = max(-int(arr[i+1])-s-summin, -int(arr[i+1])+s+summax)
            summin -= (int(arr[i+1]) + s)
            s = 0
    return int(arr[0]) + s + summax