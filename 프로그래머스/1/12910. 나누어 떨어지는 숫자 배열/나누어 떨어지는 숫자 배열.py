def solution(arr, divisor):
    L = [n for n in arr if n%divisor==0]
    return sorted(L) if L else [-1]