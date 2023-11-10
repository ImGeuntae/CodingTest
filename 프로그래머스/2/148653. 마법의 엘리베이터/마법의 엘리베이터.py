def solution(storey):
    ans = c = a = 0
    for i in str(storey)[::-1]:
        i = int(i) + c
        if i < 5:
            ans += i
            c = a = 0
        elif i > 5 or (i==5 and a):
            ans += 10-i-a
            c,a = 1,0
        else:
            ans += i
            c,a = 0,1       
    return ans + c