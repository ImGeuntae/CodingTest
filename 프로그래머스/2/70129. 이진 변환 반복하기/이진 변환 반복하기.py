def solution(s):
    step = del0 = 0
    while s!= "1":
        step += 1
        del0 += s.count("0")
        n = s.count("1")
        s = ""
        while n:
            s += str(n%2)
            n //= 2
        s = s[::-1]
    return step,del0