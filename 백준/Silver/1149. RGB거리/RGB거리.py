x=y=z=0
for _ in range(int(input())):
    r,g,b = map(int,input().split())
    x,y,z = r+min(y,z),g+min(x,z),b+min(x,y)
print(min(x,y,z))