for _ in range(int(input())):
    x = input()
    while '()' in x:
        x = x.replace('()','')
    print('NO' if x else 'YES')