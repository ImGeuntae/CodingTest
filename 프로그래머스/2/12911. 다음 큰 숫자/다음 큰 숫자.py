def solution(n):
    b = ""
    while n:
        b += str(n%2)
        n = n//2
    b += "0"
    ans = ""
    for idx, i in enumerate(b):
        if (b[:idx].count("1")) and i=="0":
            answer = ((b[:idx].count("1"))-1)*"1" + ((b[:idx].count("0"))+1)*"0" + "1" + b[idx+1:]
            return int(answer[::-1],2)