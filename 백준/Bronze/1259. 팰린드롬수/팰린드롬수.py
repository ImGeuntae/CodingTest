while (n:=input())!='0':
    for i in range(len(n)):
        if n[i] != n[-1-i]:
            print("no")
            break
    else:
        print("yes")