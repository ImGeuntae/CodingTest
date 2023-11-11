def solution(n, t, m, timetable):
    T, shuttle = [], 9*60
    for i in timetable:
        a,b = map(int,i.split(":"))
        T.append(60*a+b)
    T.sort()
    for j in range(n):
        seat = m
        for _ in range(m):
            if T and T[0] <= shuttle:
                x = T.pop(0)
                seat -= 1
        shuttle += t
    if seat:
        ans = shuttle-t
    else:
        ans = x-1
    return str((ans//60)//10)+str((ans//60)%10)+":"+str((ans%60)//10)+str((ans%60)%10)