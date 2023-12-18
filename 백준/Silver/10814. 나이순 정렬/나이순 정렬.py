L = []
for _ in range(int(input())):
    a,n = input().split()
    L += [(int(a),n)]
for i in sorted(L,key=lambda x:x[0]):
    print(*i)