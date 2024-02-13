input()
dp = [(0,0)]
for i in map(int,input().split()):
    dp += [(i,max(y for x,y in dp if i>x)+1)]
print(max(y for x,y in dp))