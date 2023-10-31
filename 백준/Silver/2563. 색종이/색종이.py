W = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(int(input())):
    x,y = map(int,input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            W[j][i] = 1
print(sum([sum(z)for z in W]))