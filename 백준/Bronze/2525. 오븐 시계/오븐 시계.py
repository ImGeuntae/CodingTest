H, M = map(int, input().split())
T = int(input()) + H*60 + M
H, M = (T//60)%24, T%60
print("{} {}".format(H, M))