def solution(n, k):
    c,answer = "",0
    while n:
        c += str(n%k)
        n //= k
    for i in c[::-1].split("0"):
        if i in ["","1"]:
            continue
        else:
            i = int(i)
            for j in range(2,int(i**0.5)+1):
                if not i%j:
                    break
            else:
                answer += 1
    return answer