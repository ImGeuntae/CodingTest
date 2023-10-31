S1 = S2 = 0
for _ in range(20):
    *others, n, g = input().split()
    if g != "P":
        g = ("FDCBA".find(g[0]))+(0.5*(g[-1]=="+"))
        S1 += g*float(n)
        S2 += float(n)
print(S1/S2)