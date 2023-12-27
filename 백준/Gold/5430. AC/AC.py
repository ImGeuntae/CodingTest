for _ in range(int(input())):
    P,_,X = input(),input(),[n for n in input()[1:-1].split(',') if n]
    r = False
    for p in P:
        if p=='R':
            r = not r
        elif X:
            X.pop(-1*(r))
        else:
            print('error')
            break
    else:
        if r:
            X = X[::-1]
        print('['+','.join(X)+']')