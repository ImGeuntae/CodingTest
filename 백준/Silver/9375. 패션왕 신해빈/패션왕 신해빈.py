for _ in range(int(input())):
    C = dict()
    for i in range(int(input())):
        a,b = input().split()
        if b in C:
            C[b] += 1
        else:
            C[b] = 2
    ans = 1
    for x in C.values():
        ans *= x
    print(ans-1)