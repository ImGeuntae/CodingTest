H, M = map(int, input().split())
T = (H*60+M)-45
if T<0:
    T += 24*60
print("{} {}".format(str(T//60), str(T%60)))