ans = int(input())
for _ in range(ans):
    L = []
    for i in input():
        if i in L and L[-1] != i:
            ans -= 1
            break
        else:
            L.append(i)
print(ans)