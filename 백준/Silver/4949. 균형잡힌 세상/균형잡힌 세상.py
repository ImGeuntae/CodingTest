while (x:=input())!=".":
    s = ''
    for i in x:
        if i in "[]()":
            s += i
    while ("()" in s) or ("[]" in s):
        s = s.replace("[]","").replace("()","")
    print("no" if s else "yes")