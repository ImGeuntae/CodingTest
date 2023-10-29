def solution(n):
    F = [0,1]
    while len(F) < n:
        F.append(F[-1]+F[-2])
    return (F[-1] + F[-2])%1234567