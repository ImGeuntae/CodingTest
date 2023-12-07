N,M = map(int,input().split())
paper = set(map(int,input().split()))
paper = [x for x in range(1,N+1) if x not in paper]
page = ans = 0
for p in paper:
    if page and 2*(p-page) < 7:
        ans += 2*(p-page)
    else:
        ans += 7
    page = p
print(ans)