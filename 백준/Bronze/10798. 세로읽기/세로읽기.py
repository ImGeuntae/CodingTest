L = [input() for _ in range(5)]
ans = ""
for i in range(15):
    for j in range(5):
        if len(L[j])>=i+1:
            ans += L[j][i]
print(ans)