def solution(n, t, m, timetable):
    T, shuttle = [], 9*60
    for i in timetable:
        T.append(60*int(i[:2])+int(i[-2:]))
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
    return str(ans//60).zfill(2)+":"+str(ans%60).zfill(2)