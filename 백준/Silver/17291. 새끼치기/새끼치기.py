a,b,c,d=0,0,0,1
for i in range(int(input())):
    a,b,c,d = b,c,d,(a*(1-i%2))+b+c+d
print(d)