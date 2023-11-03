while True:
    A,B = map(int,input().split())
    if not A and not B:
        break
    elif not A%B:
        print("multiple")
    elif not B%A:
        print("factor")
    else:
        print("neither")