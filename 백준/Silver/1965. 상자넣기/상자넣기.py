d=[0]*1001
input()
for n in map(int,input().split()):
    d[n]=max(d[:n])+1
print(max(d))