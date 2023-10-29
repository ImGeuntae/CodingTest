H, M = map(int, input().split())
T = (H*60+M)-45
print("{} {}".format(((T//60)%24), (T%60)))