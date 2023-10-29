import math
def twodiv(List):
    K = []
    m = n = 0
    for L in List:
        m += 1
        L = sorted(L)
        if L[0] != 1:
            i = math.trunc(math.log2(L[0]))
            a = 2**i
            if a != L[0]:
                K.append(sorted([a, L[1], L[2]]))
                K.append(sorted([L[0] - a, L[1], L[2]]))
            else:
                b = L[1] % L[0]
                if b != 0:
                    K.append(sorted([L[0], L[1] - b, L[2]]))
                    K.append(sorted([L[0], b, L[2]]))
                else:
                    c = L[2] % L[0]
                    if c != 0:
                        K.append(sorted([L[0], L[1], L[2] - c]))
                        K.append(sorted(([L[0], L[1], c])))
                    else:
                        K.append(L)
                        n += 1
        else:
            K.append(L)
            n += 1
    if m == n:
        c = 1
    else:
        c = 0
    return K, c
L = [sorted(map(int,input().split()))]
while True:
    L, c = twodiv(L)
    if c == 1:
        break
size = int(math.log2(L[0][0]))
d = {}
for s in range(size):
    d[str(s).zfill(2)] = 0
for K in sorted(L):
    d[str(int(math.log2(K[0]))).zfill(2)] = d.setdefault(str(int(math.log2(K[0]))).zfill(2), 0) + int(K[1]*K[2]/(K[0]**2))
dd = {}
for N in range(int(input())):
    A, B = input().split()
    dd[str(A).zfill(2)] = int(B)
count = 0
for i in dict(sorted(d.items(), reverse=True)):
    if i in dd:
        if dd[i] >= d[i]:
            count += d[i]
        else:
            if i == '00':
                count = -1
                break
            else:
                count += dd[i]
                d[str(int(i)-1).zfill(2)] += (d[i] - dd[i])*8
    else:
        if i == '00':
            count = -1
            break
        else:
            d[str(int(i)-1).zfill(2)] += d[i]*8
print(count)