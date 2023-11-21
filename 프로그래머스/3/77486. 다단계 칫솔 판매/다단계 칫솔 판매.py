def solution(enroll, referral, seller, amount):
    org, ans = dict(), dict()
    for e,r in zip(enroll, referral):
        org[e] = r
        ans[e] = 0
    for s,a in zip(seller, amount):
        a = a*100
        while s != '-' and a:
            ans[s] += a - int(a*0.1)
            s,a = org[s], int(a*0.1)
    return list(ans.values())