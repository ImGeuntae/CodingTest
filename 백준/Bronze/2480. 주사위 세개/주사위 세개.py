N = sorted(list(map(int,input().split())))
if N[0] == N[1] and N[1] == N[2]:
    print(10000+(N[1]*1000))
elif N[0] != N[1] and N[1] != N[2]:
    print(N[2]*100)
else:
    print(1000+(N[1]*100))