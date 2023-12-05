a,b,c,d = 1,1,1,0
for _ in range(int(input())):
    a,b,c,d = b,c,d,1-(a*b*d)
print(["CY","SK"][d])