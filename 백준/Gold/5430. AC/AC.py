for _ in range(int(input())):
    P,n,X = input(),int(input()),[n for n in input()[1:-1].split(',') if n]
    r,n = False,[0,n]
    for p in P:
        if p=='R':
            r = not r
        elif r:
            n[1] -= 1
        else:
            n[0] += 1
        if n[0] > n[1]:
            print('error')
            break
    else:
        X = X[n[0]:n[1]]
        if r:
            X = X[::-1]
        print('['+','.join(X)+']')