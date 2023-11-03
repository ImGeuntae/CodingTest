import sys
time = sorted([list(map(int,sys.stdin.readline().split())) for i in range(int(input()))],key=lambda x:(x[1],x[0]))
t, ans = -1, 0
for i in time:
    if i[0] >= t:
        t = i[-1]
        ans += 1
print(ans)