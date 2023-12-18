for _ in range(int(input())):
    ans = 0
    for x in input():
        if x=='(':
            ans += 1
        else:
            ans -= 1
        if ans < 0:
            print("NO")
            break
    else:
        print("NO" if ans else "YES")