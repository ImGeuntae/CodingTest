for i in range(int(input())):
    P = ""
    R, S = input().split()
    for j in str(S):
        P += j*int(R)
    print(P)