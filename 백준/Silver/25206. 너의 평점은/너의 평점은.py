G = ["D0","D+","C0","C+","B0","B+","A0","A+"]
S1 = S2 = float(0)
for _ in range(20):
    *others, n, g = input().split()
    if g == "P":
        continue
    elif g == "F":
        s = 0
    else:
        s = (0.5)*((G.index(g))+2)
    S1 += s*float(n)
    S2 += float(n)
print(S1/S2)